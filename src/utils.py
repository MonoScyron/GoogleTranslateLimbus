import time
import os
import logging
from typing import Tuple, List

import googletrans as gt
import json
import re
import shutil

from const import LANG_LIST, BUILD_PATH, WAIT_ON_ERROR, WAIT_ON_BIG_ERROR, WAIT_ON_SUCCESS, NUM_RETRY

translator = gt.Translator(
    raise_exception=True
)


def get_logger():
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler("./log.log", encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    log = logging.getLogger('GT')
    log.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    return log


LOG = get_logger()


# translate iff filename has prefix
def translate_regex(path: str, values: list[str], p: str | re.Pattern[str] = None, retry=-1):
    for filename in os.listdir(path):
        if p and not re.match(p, filename):
            continue
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


def __translate_step(text: str, lang_index: int, lang_list: List[str], retry: int = NUM_RETRY) -> Tuple[str, bool]:
    curr_try = 0
    trans_text = text
    while True:
        try:
            trans_text = translator.translate(trans_text,
                                              src=lang_list[lang_index],
                                              dest=lang_list[lang_index + 1])
            trans_text = trans_text.text
            time.sleep(WAIT_ON_SUCCESS)
        except Exception as e:
            LOG.error(f'error on text at lang_index {lang_index} '
                      f'{f"(retry {curr_try + 1} of {retry})" if retry > 0 else ""}: {e}')
            if "The block will expire shortly after those requests stop" in f'{e}':
                time.sleep(WAIT_ON_BIG_ERROR)
            else:
                time.sleep(WAIT_ON_ERROR)
            curr_try += 1
            if curr_try >= retry:
                return trans_text, False
            continue
        break
    return trans_text, True


def scramble_single(text: str, filename: str, value: str, cache=None, retry=-1, lang_list=LANG_LIST) -> str:
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
            LOG.info(f'found cached value: {t}')
            translation.append(cache[t])
        else:
            LOG.info(f'translating: {t}')
            translated = t
            for j in range(len(lang_list) - 1):
                translated, success = __translate_step(translated, j, retry=retry, lang_list=lang_list)
                if not success:
                    LOG.critical(f'failed translating in {filename}, skipping text: {t}')
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
        LOG.info(f'skip {filename}')
        return

    # if file isn't json or has no dataList, copy raw
    raw_file_path = os.path.join(local_path, filename)
    if not os.path.isfile(raw_file_path):
        LOG.info(f'{filename} not file, skipping')
        return

    if not filename.endswith('.json'):
        LOG.info(f'{filename} not json, copying raw')
        shutil.copy(raw_file_path, write_path)
        return

    data = readfile(raw_file_path)
    if 'dataList' not in data:
        LOG.info(f'{filename} has no dataList, copying raw')
        shutil.copy(raw_file_path, write_path)
        return

    cache = {}
    LOG.info(f'TRANSLATING {filename}')

    data_len = len(data['dataList'])
    for i, d in enumerate(data['dataList']):
        for v in values:
            # do not translate
            if v not in d:
                continue

            LOG.info(f'{filename}: translating ({i + 1}/{data_len}): {d[v]}')
            d[v] = scramble(d[v], filename=filename, v=v, values=values, retry=retry, cache=cache)

    writefile(write_path, data)


def scramble(dv: str | list | dict,
             filename: str = '',
             v: str = '',
             values=None,
             retry: int = -1,
             cache=None,
             lang_list=None):
    if lang_list is None:
        lang_list = LANG_LIST
    if cache is None:
        cache = {}
    if values is None:
        values = []

    if type(dv) == list:
        translated = []
        for e in dv:
            translated.append(scramble(e,
                                       filename=filename,
                                       v=v,
                                       values=values,
                                       retry=retry,
                                       cache=cache,
                                       lang_list=lang_list))
        return translated
    elif type(dv) == str:
        return scramble_single(dv, filename, v, cache=cache, retry=retry, lang_list=lang_list)
    elif type(dv) == dict:
        translated = dv
        for k in dv:
            if k in values:
                translated[k] = scramble(translated[k],
                                         filename=filename,
                                         v=v,
                                         values=values,
                                         retry=retry,
                                         cache=cache,
                                         lang_list=lang_list)
        return translated
    else:
        LOG.warning(f'unknown type {dv}={type(dv)}, returning raw value (may be PM jank)')
        return dv
