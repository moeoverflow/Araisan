#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the base for applying constriants to data for araisan.
"""

import sys
from araisan.Filter.IntegerConstraint import IngeterConstraint
from araisan.Filter.FloatConstraint import FloatConstraint
from araisan.Filter.StringConstraint import StringConstraint


class Constraint:
    """
    Parse and apply constaints
    """
    def __init__(self, datatype, constraint):
        """
        Init with all constraints
        """
        self.__filter__ = {}
        if datatype == 'csv':
            self.__parse_csv_constraint__(constraint)

    def __parse_csv_constraint__(self, constraints):
        """
        Parse CSV Constraints
        """
        for rule in range(len(constraints)):
            constraint = constraints[rule]['constriant']
            constraint.setdefault(None)
            constraint_type = constraint['type'].lower()
            if constraint_type == 'integer':
                self.__filter__[constraints[rule]['field']] = IngeterConstraint(constraint)
            elif constraint_type == 'float':
                self.__filter__[constraints[rule]['field']] = FloatConstraint(constraint)
            elif constraint_type == 'string':
                self.__filter__[constraints[rule]['field']] = StringConstraint(constraint)
            else:
                raise RuntimeError('Specified type \'%s\' not supported by Araisan yet' % (constraint_type))
