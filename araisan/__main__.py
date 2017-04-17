#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
The main entry point. Invoke as `araisan task.yaml' or `python -m araisan task.yaml'.
"""

import sys

def main():
    from .core import Araisan
    try:
        araisan_etl = Araisan(sys.argv[1])
    except StandardError:
        print("Invoke as `araisan task.yaml' or `python -m araisan task.yaml'")

if __name__ == '__main__':
    main()
