# coding=utf-8
from peewee import IntegerField, TimeField, CharField, BooleanField
from .baseModel import BaseModel


class Message(BaseModel):
    """提醒消息Model

    Attributes:
        id: 主键id
        content: 消息内容
        time: 提醒时间

    """
    id = IntegerField(primary_key=True, sequence=True)
    content = CharField(max_length=150)
    time = TimeField()

    def __init__(self, content, time):
        BaseModel.__init__(self, content=content, time=time)
