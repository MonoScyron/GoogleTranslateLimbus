import time
import os
import logging
from typing import Tuple

import googletrans as gt
import json
import re
import shutil

from const import WAIT_ON_SUCCESS, WAIT_ON_BIG_ERROR, WAIT_ON_ERROR, BUILD_PATH, NUM_RETRY

translator = gt.Translator(
    raise_exception=True
)
# english -> serbian -> marathi -> chinese -> dutch -> arabic -> korean -> polish -> hindi -> telugu -> punjabi -> english
lang_list = ['en', 'sr', 'mr', 'zh-cn', 'nl', 'ar', 'ko', 'pl', 'hi', 'te', 'pa', 'en']

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler("./log.log", encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

log = logging.getLogger('GT')
log.setLevel(logging.DEBUG)
log.addHandler(file_handler)


# translate iff filename has prefix
def translate_regex(path: str, values: list[str], p: str | re.Pattern[str] = '', retry=-1):
    for filename in os.listdir(path):
        if re.match(p, filename):
            __translate_file(filename, path, values, retry)


# normal translate
def translate(path: str, values: list[str], retry=-1):
    for filename in os.listdir(path):
        __translate_file(filename, path, values, retry)


def readfile(filepath: str) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def writefile(filepath: str, data: dict) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def __translate_step(text: str, lang_index: int, retry: int) -> Tuple[str, bool]:
    trans_text = text
    while True:
        try:
            trans_text = translator.translate(trans_text,
                                              src=lang_list[lang_index],
                                              dest=lang_list[lang_index + 1])
            trans_text = trans_text.text
            time.sleep(WAIT_ON_SUCCESS)
        except Exception as e:
            log.error(f'error on text at lang_index {lang_index} '
                      f'{f"(retry {NUM_RETRY - retry + 1} of {NUM_RETRY})" if NUM_RETRY > 0 else ""}: {e}')
            if "The block will expire shortly after those requests stop" in f'{e}':
                time.sleep(WAIT_ON_BIG_ERROR)
            else:
                time.sleep(WAIT_ON_ERROR)
            retry -= 1
            if retry == 0:
                return trans_text, False
            continue
        break
    return trans_text, True


def scramble_single(text: str, filename: str, value: str, cache=None, retry=-1) -> str:
    if cache is None:
        cache = {}

    if not any(char.isalpha() for char in text) or text[:2] == '//':
        return text

    raw_split = re.split(r"(\s*)(</?[a-z\s]*[=/].*?>|</?i>|</?b>|</?u>|\n|\[?{[0-9a-zA-Z]+}]?|\[[a-zA-Z0-9\s]+])(\s*)",
                         text)
    translation = []
    for i, t in enumerate(raw_split):
        # skip empty
        if len(t.strip()) < 1:
            translation.append(t)
            continue
        # skip text tags
        if t[0] == '<' and t[-1] == '>' and (
                '=' in t or
                '/' in t or
                t == '<i>' or
                t == '<u>' or
                t == '<b>'
        ):
            translation.append(t)
            continue
        # skip escape vars
        if t == '\n' or re.match(r'\[?{[0-9a-zA-Z]+}]?|\[[a-zA-Z0-9\s]+]', t):
            translation.append(t)
            continue
        # skip Clue for clue specifically
        if value == 'clue' and t == 'Clue':
            translation.append(t)
            continue

        if t in cache:
            log.info(f'found cached value: {t}')
            translation.append(cache[t])
        else:
            log.info(f'translating: {t}')
            translated = t
            for j in range(len(lang_list) - 1):
                translated, success = __translate_step(translated, j, retry)
                if not success:
                    log.critical(f'failed translating in {filename}, skipping text: {t}')
                    translated = t
                    break
            cache[t] = translated
            translation.append(translated)

    return ''.join(translation)


def __translate_file(filename: str, local_path: str, values: list[str], retry: int):
    write_path = os.path.join(BUILD_PATH, local_path, filename)
    os.makedirs(os.path.dirname(write_path), exist_ok=True)

    # skip if translation already exists
    if filename in os.listdir(os.path.join(BUILD_PATH, local_path)):
        log.info(f'skip {filename}')
        return

    # if file isn't json or has no dataList, copy raw
    raw_file_path = os.path.join(local_path, filename)
    if not os.path.isfile(raw_file_path):
        log.info(f'{filename} not file, skipping')
        return

    if not filename.endswith('.json'):
        log.info(f'{filename} not json, copying raw')
        shutil.copy(raw_file_path, write_path)
        return

    data = readfile(raw_file_path)
    if 'dataList' not in data:
        log.info(f'{filename} has no dataList, copying raw')
        shutil.copy(raw_file_path, write_path)
        return

    cache = {}
    log.info(f'TRANSLATING {filename}')

    data_len = len(data['dataList'])
    for i, d in enumerate(data['dataList']):
        for v in values:
            # do not translate
            if v not in d:
                continue

            log.info(f'{filename}: translating ({i + 1}/{data_len}): {d[v]}')
            d[v] = scramble(d[v], filename=filename, v=v, values=values, retry=retry, cache=cache)

    writefile(write_path, data)


def scramble(dv: str | list | dict, filename: str = '', v: str = '', values=None, retry: int = -1, cache=None):
    if cache is None:
        cache = {}
    if values is None:
        values = []

    if type(dv) == list:
        translated = []
        for e in dv:
            translated.append(scramble(e, filename=filename, v=v, values=values, retry=retry, cache=cache))
        return translated
    elif type(dv) == str:
        return scramble_single(dv, filename, v, cache=cache, retry=retry)
    elif type(dv) == dict:
        translated = dv
        for k in dv:
            if k in values:
                translated[k] = scramble(translated[k], filename=filename, v=v, values=values, retry=retry, cache=cache)
        return translated
    else:
        log.warning(f'unknown type {dv}={type(dv)}, returning raw value (may be PM jank)')
        return dv
