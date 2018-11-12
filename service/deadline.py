# coding=utf-8
import datetime
from model.message import Message
from model.deadline import Deadline


class DeadlineService(object):

    def __init__(self):
        self.__text_dict = {
            "week_flag": "一星期",
            "three_days_flag": "三天",
            "day_flag": "最后一天"
        }

    def add(self, json_dict: dict) -> bool:
        for key in self.text_dict.keys:
            if json_dict[key]:
                msg = Message("[提醒]距离DDL：%s 到期还有%s" % (json_dict["title"], self.__text_dict[key]),
                              self.__get_time_str(json_dict["time"], key))
                msg.save()
                json_dict[key] = msg.id
        # 保存deadline对象
        deadline = self.__get_deadline(json_dict)
        line = deadline.save()
        return line > 0

    def update(self, ddl_id: int, json_dict: dict) -> bool:
        deadline = self.__get_deadline(json_dict)
        deadline.id = ddl_id
        ddl_line = deadline.update()
        for key in self.text_dict.keys:
            if json_dict[key]:
                msg = Message("[提醒]距离DDL：%s 到期还有%s" % (json_dict["title"], self.text_dict[key]),
                              self.__get_time_str(json_dict["time"], key))
                msg.update()
        return ddl_line > 0

    def get(self, ddl_id: int) -> dict:
        deadline = Deadline.get_by_id(ddl_id)
        if deadline is not None:
            return deadline.dicts()
        else:
            return {}

    def get_list(self, type_str: str) -> iter:
        deadline_dicts = []
        if type_str == "all":
            deadline_dicts = Deadline.select().dicts()
        elif type_str == "active":
            deadline_dicts = Deadline.select().where(Deadline.finish_time is not None).dicts()
        return deadline_dicts

    def __get_deadline(self, json_dict: dict) -> Deadline:
        return Deadline(
            time=json_dict["time"],
            title=json_dict["title"],
            detail=json_dict["detail"],
            week_flag=json_dict["week_flag"],
            three_days_flag=json_dict["three_days_flag"],
            day_flag=json_dict["day_flag"]
        )

    def __get_time_str(self, time_str: str, time_flag: str) -> str:
        time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        time_dict = {
            "week_flag": self.__minus_days(time, 7),
            "three_days_flag": self.__minus_days(time, 3),
            "day_flag": self.__minus_days(time, 1)
        }
        return time_dict[time_flag]

    def __minus_days(self, time: datetime.datetime, day_num: int) -> str:
        return (time - datetime.timedelta(day_num)).strftime("%Y-%m-%d %H:%M:%S")
