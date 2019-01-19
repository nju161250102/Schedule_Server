# coding=utf-8
from datetime import datetime, timedelta
import json
import requests
from config import Config
from task import Task
from service.msgService import MsgService
from service.planService import PlanService


class MinuteTask(Task):

    def __init__(self, logger):
        # set the interval: 60 sec = 1 minute
        super().__init__(60, logger)
        self.offset = None
        self.command = None

    def t_send_msg(self):
        for msg in MsgService.get_msg():
            post_data = {
                "chat_id": Config.get("USER_ID"),
                "text": msg["content"]
            }
            r = requests.post(Config.get("TOKEN_URL") + "sendMessage", data=post_data)
            if r.status_code == 200:
                self.logger.info("Send Message: ID " + str(msg["id"]))

    def t_remind(self):
        now_time = datetime.now().strftime("%H:%M")
        if now_time in ["07:59", "13:59", "18:29"]:
            plan_list = PlanService.todo_list()
            result = ["◈计划清单◈"]
            for plan in plan_list:
                result.append("ID: %s\tTime: %s" % (plan["id"], plan["create_time"]))
                result.append(plan["detail"])
            MsgService.save("\n".join(result), self._next_minute())

    def t_get_msg(self):
        query_str = "" if self.offset is None else "?offset=" + str(self.offset)
        r = requests.get(Config.get("TOKEN_URL") + "getUpdates" + query_str)
        if r.status_code == 200:
            data = json.loads(r.text, encoding="utf-8")
            if data["ok"]:
                for update_msg in data["result"]:
                    msg = update_msg["message"]
                    if "entities" in msg.keys() and len(msg["entities"]) == 1:
                        length = msg["entities"][0]["length"]
                        self.command = getattr(self, "_" + msg["text"][1:length])
                    elif "entities" not in msg.keys():
                        if self.command is not None:
                            self.command(msg["text"])
                            self.command = None
                    self.offset = update_msg["update_id"] + 1
        requests.get(Config.get("TOKEN_URL") + "getUpdates?offset=" + str(self.offset))

    def _todo(self, text: str):
        if "\n" not in text:
            return
        split_index = text.index("\n")
        priority = int(text[:split_index])
        result = PlanService.add(text[split_index + 1:], priority)
        if result != 0:
            MsgService.save("待办事项（ID：%s）已加入" % str(result), self._next_minute())
        else:
            self.logger.error("待办事项保存失败")

    def _finish(self, text: str):
        array = text.split("\n")
        ok_list = []
        error_num = 0
        for item in array:
            if item.isdigit():
                result = PlanService.finish(int(item))
            else:
                result = PlanService.add(item, PlanService.FINISHED)
            if result:
                ok_list.append(item)
            else:
                error_num += 1
        if len(ok_list) == 0:
            MsgService.save("完成确认失败", self._next_minute())
        else:
            MsgService.save("确认完成的计划ID：%s" % (", ".join(ok_list),), self._next_minute())
        self.logger.info("完成计划ID：" + ", ".join(ok_list))
        if error_num != 0:
            self.logger.error("出现错误数目：" + str(error_num))

    def _delete(self, text: str):
        array = text.split("\n")
        ok_list = []
        error_num = 0
        for item in array:
            if item.isdigit() and PlanService.delete(int(item)):
                ok_list.append(item)
            else:
                error_num += 1
        if len(ok_list) == 0:
            MsgService.save("计划删除失败", self._next_minute())
        else:
            MsgService.save("删除成功的计划ID：%s" % (", ".join(ok_list),), self._next_minute())
        self.logger.info("删除的ID：" + ", ".join(ok_list))
        if error_num != 0:
            self.logger.error("出现错误数目：" + str(error_num))

    def _next_minute(self):
        new_time = datetime.now() + timedelta(minutes=1)
        return new_time.strftime("%Y-%m-%d %H:%M")
