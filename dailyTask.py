# coding=utf-8
import json
import requests
from datetime import datetime
from task import Task
from config import Config
from service.lessonService import LessonService
from service.msgService import MsgService


class DailyTask(Task):

    def __init__(self, logger):
        # set the interval: 60*60*24 sec = 1 day
        super().__init__(60*60*24, logger)

    def t_get_lesson(self):
        lessons = LessonService.get_lessons()
        for lesson in lessons:
            text = "\n".join(["◈课程提醒◈", lesson["name"], lesson["classroom"]])
            seconds = (datetime.strptime(lesson["time"], "%H:%M") - datetime.strptime("00:30", "%H:%M")).total_seconds()
            msg_date = datetime.now()
            msg_date = msg_date.replace(hour=int(seconds / 3600), minute=int((seconds % 3600) / 60))
            if MsgService.save(text, msg_date.strftime("%Y-%m-%d %H:%M")) == 0:
                self.logger.error("There are something wrong while importing lessons")
        self.logger.info("Today's Lessons saved to message")

    def t_get_weather(self):
        city = Config.get("CITY_CODE")
        r = requests.get("http://t.weather.sojson.com/api/weather/city/" + city)
        data = json.loads(r.text, encoding="utf-8")
        text = "\n".join(["◈每日天气◈",
                          data["data"]["forecast"][0]["ymd"] + " " + data["data"]["forecast"][0]["week"],
                          data["data"]["forecast"][0]["high"],
                          data["data"]["forecast"][0]["low"],
                          data["data"]["forecast"][0]["fx"] + " " + data["data"]["forecast"][0]["fl"],
                          "天气 " + data["data"]["forecast"][0]["type"]
                          ])
        msg_date = datetime.now()
        msg_date = msg_date.replace(hour=7, minute=0)
        if MsgService.save(text, msg_date.strftime("%Y-%m-%d %H:%M")) == 0:
            self.logger.error("There are something wrong while saving weather")
        self.logger.info("Weather info saved to message")
