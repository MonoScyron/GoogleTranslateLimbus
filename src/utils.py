from datetime import datetime

import time
import os
from typing import Any

import googletrans as gt
import json
import re

BUILD_PATH = './release'
WAIT_ON_ERROR = 60
WAIT_ON_BIG_ERROR = 600
WAIT_ON_SUCCESS = .33

translator = gt.Translator(
    raise_exception=True
)
# english -> serbian -> marathi -> chinese -> dutch -> arabic -> korean -> polish -> hindi -> telugu -> punjabi -> english
lang_list = ['en', 'sr', 'mr', 'zh-cn', 'nl', 'ar', 'ko', 'pl', 'hi', 'te', 'pa', 'en']


# translate iff filename has prefix
def translate_prefix(path: str, values: list[str], prefix='', retry=-1):
    for filename in os.listdir(path):
        if filename.startswith(prefix):
            __translate_file(filename, path, values, retry)


# normal translate
def translate(path: str, values: list[str], retry=-1):
    for filename in os.listdir(path):
        __translate_file(filename, path, values, retry)


def __readfile(filepath: str) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def __writefile(filepath: str, data: dict) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def __translate_step(text: str, lang_index: int, retry: int) -> str:
    trans_text = text
    while retry != 0:
        try:
            trans_text = translator.translate(trans_text,
                                              src=lang_list[lang_index],
                                              dest=lang_list[lang_index + 1])
            trans_text = trans_text.text
            time.sleep(WAIT_ON_SUCCESS)
        except Exception as e:
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - error on text at lang_index {lang_index}: {e}')
            if "The block will expire shortly after those requests stop" in f'{e}':
                time.sleep(WAIT_ON_BIG_ERROR)
            else:
                time.sleep(WAIT_ON_ERROR)
            retry -= 1
            continue
        break
    return trans_text


def scramble_single(text: str, value: str, retry=-1) -> str:
    if not any(char.isalpha() for char in text) or text[:2] == '//':
        return text

    translation = re.split(r"(</?[a-z]*[=/].*?>|</?i>|</?b>|\n|\[?{[0-9a-zA-Z]+}]?|\[[a-zA-Z0-9\s]+])", text)
    for i, t in enumerate(translation):
        # skip empty
        if len(t) < 1:
            continue
        # skip text tags
        if t[0] == '<' and t[-1] == '>' and (
                '=' in t or
                '/' in t or
                t == '<i>' or
                t == '<b>'
        ):
            continue
        # skip escape vars
        if t == '\n' or re.match(r'\[?{[0-9a-zA-Z]+}]?|\[[a-zA-Z0-9\s]+]', t):
            continue
        # skip Clue for clue specifically
        if value == 'clue' and t == 'Clue':
            continue

        translated = t
        for j in range(len(lang_list) - 1):
            translated = __translate_step(translated, j, retry)
        translation[i] = translated

    return ''.join(translation)


def __translate_file(filename: str, local_path: str, values: list[str], retry: int):
    write_path = os.path.join(BUILD_PATH, local_path, filename)
    os.makedirs(os.path.dirname(write_path), exist_ok=True)

    # skip if translation already exists or if file isn't json
    if not filename.endswith('.json') or filename in os.listdir(os.path.join(BUILD_PATH, local_path)):
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - skip {filename}')
        return

    data = __readfile(os.path.join(local_path, filename))
    if 'dataList' not in data:
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - no dataList in {filename}, skipping')
        return

    cache = {}
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - TRANSLATING {filename}')

    data_len = len(data['dataList'])
    for i, d in enumerate(data['dataList']):
        for v in values:
            # do not translate
            if v not in d:
                continue

            if d[v] in cache:
                print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - translating from cache ({i + 1}/{data_len}): {d[v]}')
                d[v] = cache[d[v]]
            else:
                print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - translating & caching ({i + 1}/{data_len}): {d[v]}')
                d[v] = scramble(d[v], v, values, retry=retry)
                if type(d[v]) == str:
                    cache[d[v]] = d[v]

    __writefile(write_path, data)


def scramble(dv: str | list | dict, v: str, values: list[str], retry: int):
    if type(dv) == list:
        translated = []
        for e in dv:
            translated.append(scramble(e, v, values, retry))
        return translated
    elif type(dv) == str:
        return scramble_single(dv, v, retry=retry)
    elif type(dv) == dict:
        translated = dv
        for k in dv:
            if k in values:
                translated[k] = scramble(translated[k], v, values, retry)
        return translated
    else:
        raise ValueError(f'dv is unknown type: {type(dv)}')
