#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Aimed to build a handy data cleaning module 
  with support for various data type. Using
  YAML for describing a data cleaning task.
"""
__version__ = '0.0.1a'
__author__ = '0xBBC'
__licence__ = 'MIT'

try:
    import yaml
except ImportError:
    raise ImportError('Araisan needs PyYAML module to function')
