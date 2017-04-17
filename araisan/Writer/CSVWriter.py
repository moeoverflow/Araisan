#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the support of CSV file for araisan.
"""

import sys
import csv


class CSVWriter:
    """
    CSV Writer
    """
    def __init__(self, datatarget, config):
        """
        Init CSVWriter with datatarget and config
        """
        self.__csvfile__ = open(datatarget, 'w')
        self.__writer__ = csv.DictWriter(self.__csvfile__, config['fieldnames'])
        self.__writer__.writeheader()

    def __write__(self, data):
        """
        This writes data to predefined datatarget
        """
        self.__writer__.writerow(data)
