# -*- coding:utf-8 -*-
from peewee import Model, SqliteDatabase
db = SqliteDatabase('schedule.db')  # 配置数据库连接


class BaseModel(Model):

    class Meta(object):
        database = db
