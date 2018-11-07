# coding=utf-8
import datetime
from peewee import IntegerField, DateTimeField, CharField
from .baseModel import BaseModel


class Deadline(BaseModel):
    id = IntegerField(primary_key=True)
    time = DateTimeField()
    title = CharField(max_length=30)
    detail = CharField(max_length=150)
    create_time = DateTimeField(default=datetime.datetime.now())
    finish_time = DateTimeField(default=None)
    week_flag = IntegerField(default=None)
    three_days_flag = IntegerField(default=None)
    day_flag = IntegerField(default=None)
