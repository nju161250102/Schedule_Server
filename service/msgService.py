# coding=utf-8
import time
from model.message import Message


class MsgService(object):

    def clear(self):
        pass

    def get_msg(self):
        now = time.strftime("%H:%M", time.localtime())
        msg_list = Message.select().where(Message.time == now)
        return msg_list.dicts()
