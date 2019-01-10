# coding=utf-8
import requests
from config import Config
from task import Task
from service.msgService import MsgService


class MinuteTask(Task):

    def __init__(self, logger):
        # set the interval: 60 sec = 1 minute
        super().__init__(60, logger)

    def _send_msg(self):
        for msg in MsgService.get_msg():
            post_data = {
                "chat_id": Config.get("USER_ID"),
                "text": msg["content"]
            }
            r = requests.post(Config.get("TOKEN_URL") + "sendMessage", data=post_data)
            if r.status_code == 200:
                self.logger.info("Send Message: " + msg["content"])
