# coding=utf-8


class Task(object):

    def __init__(self, interval, logger):
        self.interval = interval
        self.logger = logger

    def run(self):
        method_list = list(filter(lambda s: s[0] == 't', self.__dir__()))
        for method_name in method_list:
            method = getattr(self, method_name)
            method()
