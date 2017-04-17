#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the support of CSV file for araisan.
"""

import sys
import csv


class CSVReader:
    """
    CSV Reader
    """
    def __init__(self, datasource, config):
        """
        Init CSVReader with datasource and config
        """
        self.__csvfile__ = open(datasource)
        self.__reader__ = csv.DictReader(self.__csvfile__, delimiter=config['delimiter'], quotechar=config['quotechar'])

    def fieldnames(self):
        """
        This returns all the fieldname in this CSV
        """
        return self.__reader__.fieldnames

    def __run__(self, reads):
        """
        Iterate all data from current CSV
        """
        for row in self.__reader__:
            reads(row)
