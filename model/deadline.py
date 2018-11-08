# coding=utf-8
import datetime
from peewee import IntegerField, DateTimeField, CharField
from .baseModel import BaseModel


class Deadline(BaseModel):
    """截止时间Model

    Attributes:
        id: 主键自增ID
        time: 设定的截止时间
        title: ddl标题
        detail: 详情描述
        create_time: 创建时间[default: 当前时间]
        finish_time: 完成时间[None: 未完成]
        week_flag: 周提醒ID[None: 不提醒]
        three_days_flag: 三日提醒ID[None: 不提醒]
        day_flag: 日提醒ID[None: 不提醒]

    """
    id = IntegerField(primary_key=True, sequence=True)
    time = DateTimeField()
    title = CharField(max_length=30)
    detail = CharField(max_length=150, default="")
    create_time = DateTimeField(default=datetime.datetime.now())
    finish_time = DateTimeField(default=None)
    week_flag = IntegerField(default=None)
    three_days_flag = IntegerField(default=None)
    day_flag = IntegerField(default=None)
