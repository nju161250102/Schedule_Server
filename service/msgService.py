# coding=utf-8
import time
from model import Message


class MsgService(object):

    @staticmethod
    def get_msg():
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        msg_list = Message.select().where(Message.time == now)
        return msg_list.dicts()

    @staticmethod
    def save(content, msg_time):
        msg = Message()
        msg.content = content
        msg.time = msg_time
        return msg.save()
