# coding=utf-8
from peewee import IntegerField, DateTimeField, CharField, BooleanField
from .baseModel import BaseModel


class Message(BaseModel):
    id = IntegerField(primary_key=True)
    content = CharField(max_length=150)
    time = DateTimeField()
    read_flag = BooleanField(default=False)
