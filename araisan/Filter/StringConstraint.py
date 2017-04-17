#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the String constriants to data for araisan.
"""

import re


class StringConstraint:
    """
    Parse and apply constaints
    """
    def __init__(self, constraint):
        """
        Init with all constraints
        """
        self.__filter__ = []
        if constraint.get('prefix', None):
            constraint_prefix = constraint['prefix']

            def prefix_check(x):
                for prefix in constraint_prefix:
                    if x.startswith(str(prefix)):
                        return True
                return False
            self.__filter__.append(prefix_check)
        if constraint.get('contain', None):
            constraint_contain = constraint['contain']

            def contain_check(x):
                for contain in constraint_contain:
                    if contain in x:
                        return True
                return False
            self.__filter__.append(contain_check)
        if constraint.get('suffix', None):
            constraint_suffix = constraint['suffix']

            def suffix_check(x):
                for suffix in constraint_suffix:
                    if x.endswith(str(suffix)):
                        return True
                return False
            self.__filter__.append(suffix_check)
        if constraint.get('equals', None):
            constraint_equals = constraint['equals']
            self.__filter__.append(lambda x: x in constraint_equals)
        if constraint.get('length', None):
            constraint_length = constraint['length']
            constraint_length.setdefault(None)
            if constraint_length['min']:
                self.__filter__.append(lambda x: len(x) >= constraint_length['min'])
            if constraint_length['max']:
                self.__filter__.append(lambda x: len(x) <= constraint_length['max'])
        if constraint.get('regex', None):
            constraint_regex = constraint['regex']
            regex = re.compile(constraint_regex)
            self.__filter__.append(lambda x: regex.match(x) != None)
        if bool(constraint.get('unique', None)):
            self.__seen__ = {}

            def unique_check(x):
                if self.__seen__.get(x, None) != None:
                    return False
                else:
                    self.__seen__[x] = True
                return True
            self.__filter__.append(unique_check)
        self.__allow_null__ = bool(constraint.get('allow_null', None))

    def feed(self, data):
        """
        Feed data to this IntegerConstraint
        """
        flag = True
        if data is None and self.__allow_null__ is False:
            flag = False
        else:
            for f in self.__filter__:
                flag = f(data)
                if not flag:
                    break
        return flag
