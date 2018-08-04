# util.py
"""
dirmark utils
"""

import os
import json
import copy

DIRMARK_VERSION = "0.1.0"
DIRMARK_TEMPLATE_OF = {
    "0.1.0": {
        "version": "0.1.0",
        "group": {},
    },
}

def get_default_group(vim):
    """
    get default group name
    """
    return vim.call('dirmark#get_default_group')

def new_dirmark_dict():
    """
    return template dirmark dictionary
    """
    return copy.deepcopy(DIRMARK_TEMPLATE_OF[DIRMARK_VERSION])

def write(vim, dirmark_dict):
    """
    write dirmark data to dirmark file
    """
    if not os.path.isdir(__get_cache_directory_path(vim)):
        os.makedirs(__get_cache_directory_path(vim))

    with open(__get_cache_file_path(vim), 'w') as f:
        f.write(json.dumps(dirmark_dict))

def read(vim):
    """
    open and read dirmark data, and return as dictionary
    except FileNotFoundError
    """
    # TODO: switch parse logic by version
    with open(__get_cache_file_path(vim)) as f:
        data = f.read()
        return json.loads(data)

def __get_cache_directory_path(vim):
    return vim.call('dirmark#get_cache_directory_path')

def __get_cache_file_path(vim):
    return vim.call('dirmark#get_cache_file_path')

def main(): pass

if __name__ == '__main__': main()
