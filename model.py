# -*- coding:utf-8 -*-
from peewee import Model, SqliteDatabase
from peewee import IntegerField, TextField, DateField, DateTimeField
db = SqliteDatabase('schedule.db')  # 配置数据库连接


class BaseModel(Model):

    class Meta(object):
        database = db


class Message(BaseModel):

    id = IntegerField(primary_key=True, sequence=True)
    content = TextField()
    time = TextField()

    def __init__(self, content, time):
        BaseModel.__init__(self, content=content, time=time)


class Term(BaseModel):

    id = IntegerField(primary_key=True, sequence=True)
    start = DateField(formats="%Y-%m-%d")
    end = DateField(formats="%Y-%m-%d")


class Lesson(BaseModel):

    id = IntegerField(primary_key=True, sequence=True)
    name = TextField()
    classroom = TextField()
    term = IntegerField()
    week = IntegerField()
    weekday = IntegerField()
    time = TextField()


class Deadline(BaseModel):

    id = IntegerField(primary_key=True, sequence=True)
    time = DateTimeField(formats="%Y-%m-%d %H:%M:%S")
    title = TextField()
    detail = TextField(default="")
    finish_time = DateTimeField(default=None, formats="%Y-%m-%d %H:%M:%S")
