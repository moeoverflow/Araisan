#!/usr/bin/env python
# -*- coding:utf-8 -*-    
class Araisan:
    def __init__(self, task):
        try:
            import yaml
        except ImportError:
            raise ImportError('Araisan needs PyYAML module to function')
        if type(task) == str and len(task) > 0:
            self.task_path = task
            try:
                self.task = yaml.load(open(self.task_path))
            except FileNotFoundError:
                raise FileNotFoundError("(#ﾟДﾟ)找不到'%s'啦！公园的危机！" % (task))
    def dump(self):
        print(self.task)
