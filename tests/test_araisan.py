#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""High-level tests."""

import os
import sys
import pytest

from araisan.core import Araisan

BASEDIR = os.path.dirname(__file__)


def test_load_task():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    assert r.loaded()


def test_description():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    assert (r.description() == 'Example Data Cleaning Task')


def test_run():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        r.run()
        assert os.path.isfile(os.path.abspath(os.path.join(BASEDIR, '..', 'example/score.etl.csv')))


def test_add_single_pre_hook():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        called = [False]

        def prehook(data):
            called[0] = True
            return True
        r.add_hook('pre-etl', prehook)
        r.run()
    assert called


def test_add_multi_pre_hook():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        called = [False for _ in range(3)]

        def prehook1(data):
            called[0] = True
            return True

        def prehook2(data):
            called[1] = True
            return True

        def prehook3(data):
            called[2] = True
            return True
        r.add_hook('pre-etl', prehook1)
        r.add_hook('pre-etl', prehook2)
        r.add_hook('pre-etl', prehook3)
        r.run()
    assert (called[0] and called[1] and called[2])


def test_add_single_post_hook():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        called = [False]

        def posthook(data):
            called[0] = True
            return True
        r.add_hook('post-etl', posthook)
        r.run()
    assert called


def test_add_multi_post_hook():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        called = [False for _ in range(3)]

        def posthook1(data):
            called[0] = True
            return True

        def posthook2(data):
            called[1] = True
            return True

        def posthook3(data):
            called[2] = True
            return True
        r.add_hook('post-etl', posthook1)
        r.add_hook('post-etl', posthook2)
        r.add_hook('post-etl', posthook3)
        r.run()
    assert (called[0] and called[1] and called[2])


def test_pre_post_hook_order():
    r = Araisan(os.path.abspath(os.path.join(BASEDIR, '..', 'example/example.yaml')))
    if r.loaded():
        called = [0, 0]
        called_order = [0]

        def prehook(data):
            if called[0] == 0:
                called_order[0] += 1
                called[0] = called_order[0]
            return True

        def posthook(data):
            if called[1] == 0:
                called_order[0] += 1
                called[1] = called_order[0]
            return True
        r.add_hook('pre-etl', prehook)
        r.add_hook('post-etl', posthook)
        r.run()
    assert (called[0] == 1 and called[1] == 2)
