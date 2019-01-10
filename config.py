# coding=utf-8
import json


class Config(object):

    data = {}

    @classmethod
    def refresh(cls):
        with open('config.json', 'r') as f:
            cls.data = json.load(f)

    @classmethod
    def get(cls, key):
        if key in cls.data.keys():
            return cls.data[key]
        return None
