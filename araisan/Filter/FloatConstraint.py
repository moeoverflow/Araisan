#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the Float constriants to data for araisan.
"""


class FloatConstraint:
    """
    Parse and apply constaints
    """
    def __init__(self, constraint):
        """
        Init with all constraints
        """
        self.__filter__ = []
        if constraint.get('range', None):
            constraint_range = constraint['range']
            range_start = constraint_range.get('start', None)
            range_end = constraint_range.get('end', None)
            if range_start:
                self.__filter__.append(lambda x: x >= float(range_start))
            if range_end:
                self.__filter__.append(lambda x: x <= float(range_end))
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
        Feed data to this FloatConstraint
        """
        data = float(data)
        flag = True
        if data is None and self.__allow_null__ is False:
            flag = False
        else:
            for f in self.__filter__:
                flag = f(data)
                if not flag:
                    break
        return flag
