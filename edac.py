#!/usr/bin/env python3

import os
import json
import re

DIR = '/sys/devices/system/edac/mc'

VARS = [
    'dimm_ce_count',
    'dimm_ue_count',
    'dimm_label',
    'dimm_location',
    'dimm_mem_type',
    'size'
]


def lst(dir, rgx):
    return [x for x in os.listdir(dir) if re.match(rgx, x)]


def parse(v):
    for t in [int, float]:
        try:
            return t(v)
        except BaseException:
            continue

    return v


def rv(fn):
    with open(fn, 'r') as f:
        return parse(f.read().rstrip())


def read_dimm(dir):
    return {
        x: rv(f'{dir}/{x}') for x in VARS
    }


r = {}
if os.path.exists(DIR):
    for mc in lst(DIR, r'^mc\d+$'):
        for dimm in lst(f'{DIR}/{mc}', r'^(dimm|rank)\d+$'):
            r[f'{mc}_{dimm}'] = {
                'name': f'{mc}_{dimm}',
                **read_dimm(f'{DIR}/{mc}/{dimm}')
            }

print(json.dumps(r, indent=2, sort_keys=True))
