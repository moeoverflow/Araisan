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
            self.task_path = task
            try:
                self.task = yaml.load(open(self.task_path))
            except FileNotFoundError:
                raise FileNotFoundError("(#ﾟДﾟ)找不到'%s'啦！公园的危机！" % (task))
            self.task_loaded = True
    def task_loaded():
        return self.task_loaded
        
    def dump(self):
        print(self.task)
