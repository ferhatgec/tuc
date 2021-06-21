#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#
# tuc - generate short link/s from terminal. (executable, library)
#
# github.com/ferhatgec/tuc

from requests import get
from sys import argv

link = 'https://tinyurl.com/api-create.php?url={web}'

def get_link(website: str) -> str:
    return get(link.format(web=website)).text

if len(argv) < 2:
    print('Tuc - TinyUrl CLI')
    exit(1)

for index, arg in enumerate(argv):
    if index == 0:
        continue

    print(f'{arg} -> {get_link(arg)}')