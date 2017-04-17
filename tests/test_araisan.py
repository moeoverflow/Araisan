#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""High-level tests."""
import os
import pytest

from araisan.core import Araisan

BASEDIR = os.path.dirname(__file__)


def test_load_task():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    assert r.loaded()
