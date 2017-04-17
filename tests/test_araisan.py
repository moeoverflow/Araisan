#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""High-level tests."""
import os
import pytest

BASEDIR = os.path.dirname(__file__)

from araisan.core import Araisan

def test_load_task():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    assert r.loaded()
