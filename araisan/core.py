#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This module provides the main functionality of araisan.
Invocation flow:
    1. Read, validate and process the input yaml file (args, `stdin`).
    2. Access and extract data from datasource
    3. For each data
       - Invoke the hook before data cleaning
       - Apply constraints defined in yaml
       - Invoke the hook after data cleaning
    4. Write to datatarget
    5. Exit.
"""

import sys
import yaml


class Araisan:
    """
    アライさんにおまかせなのだ！
    """
    def __init__(self, task):
        """
        Init Araisan with the path to yaml file describes
          data cleaning task
        """
        if type(task) == str and len(task) > 0:
            self.__task_path__ = task
            try:
                self.__task__ = yaml.load(open(self.__task_path__))
            except FileNotFoundError:
                raise FileNotFoundError("(#ﾟДﾟ)找不到'%s'啦！公园的危机！" % (task))
            self.__description__ = self.__task__['description']
            self.__datatype__ = self.__task__['datatype'].lower()
            self.__load__()
            # Hooks before data cleaning
            self.__pre_etl__ = []
            # Hooks after data cleaning
            self.__post_etl__ = []

    def add_hook(self, process_position, hook):
        """
        Add hook to process_position, either 'pre-etl' or 'post-etl'
        """
        if process_position == 'pre-etl':
            self.__pre_etl__.append(hook)
        elif process_position == 'post-etl':
            self.__post_etl__.append(hook)
        else:
            raise StandardError('%s - No such process position to add a hook' % (process_position))

    def description(self):
        """
        This gives the description of current data cleaning task
        """
        return self.__description__

    def loaded(self):
        """
        True if Araisan handled the given YAML correctly
        """
        return self.__task_loaded__

    def run(self):
        """
        Start the data cleaning task
        """
        def __reader_callback__(data):
            flag = True
            for prehook in self.__pre_etl__:
                flag = prehook(data)
                if not flag:
                    break
            if not flag:
                return
            for k in self.__constraint__.__filter__.keys():
                flag = self.__constraint__.__filter__[k].feed(data[k])
                if not flag:
                    break
            if not flag:
                return
            for posthook in self.__post_etl__:
                flag = posthook(data)
                if not flag:
                    break
            if flag:
                self.__writer__.__write__(data)
        self.__reader__.__run__(__reader_callback__)

    def __load__(self):
        """
        Load datasource, constraints
        """
        self.__load_config__()
        self.__load_datasource__()
        self.__load_constraint__()
        self.__load_datatarget__()
        self.__task_loaded__ = True

    def __load_datasource__(self):
        """
        Load data source according to datatype
        """
        if self.__datatype__ == 'csv':
            from .Reader.CSVReader import CSVReader
            self.__reader__ = CSVReader(self.__task__['datasource'], self.__config__)
            self.__config__['fieldnames'] = self.__reader__.fieldnames()
        else:
            raise RuntimeError('Araisan does not support %s yet' % (self.__datatype__))

    def __load_config__(self):
        """
        Load config for the very datatype
        """
        if self.__datatype__ == 'csv':
            config = {
                'delimiter': ',',
                'quotechar': '\''
            }
            if self.__task__.get('config', None):
                task_config = self.__task__['config']
                if task_config.get('delimiter', None):
                    config['delimiter'] = task_config['delimiter']
                if task_config.get('quotechar', None):
                    config['quotechar'] = task_config['quotechar']
            self.__config__ = config
        else:
            raise RuntimeError('Araisan does not support %s yet' % (self.__datatype__))

    def __load_datatarget__(self):
        """
        Load datatarget
          if datatarget == 'custom'
          then user needs to set a callback via pretty_data(last)
        """
        task_datatarget = self.__task__['datatarget']
        if task_datatarget != 'custom':
            if self.__datatype__ == 'csv':
                from .Writer.CSVWriter import CSVWriter
                self.__writer__ = CSVWriter(task_datatarget, self.__config__)
            else:
                raise RuntimeError('Araisan does not support %s yet' % (self.__datatype__))

    def __load_constraint__(self):
        """
        Load constraints on data
        """
        from .Filter.Constraint import Constraint
        self.__constraint__ = Constraint(self.__datatype__, self.__task__['rules'])
