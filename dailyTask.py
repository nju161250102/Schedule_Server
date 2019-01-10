# coding=utf-8
from datetime import datetime
from task import Task
from service.lessonService import LessonService
from service.msgService import MsgService


class DailyTask(Task):

    def __init__(self, logger):
        # set the interval: 60*60*24 sec = 1 day
        super().__init__(60*60*24, logger)

    def _get_lesson(self):
        lessons = LessonService.get_lessons()
        for lesson in lessons:
            text = "\n".join(["◈课程提醒◈", lesson["name"], lesson["classroom"]])
            seconds = (datetime.strptime(lesson["time"], "%H:%M") - datetime.strptime("00:30", "%H:%M")).total_seconds()
            msg_date = datetime.now()
            msg_date = msg_date.replace(hour=int(seconds / 3600), minute=int((seconds % 3600) / 60))
            if MsgService.save(text, msg_date.strftime("%Y-%m-%d %H:%M")) == 0:
                self.logger.error("There are something wrong while importing lessons")
        self.logger.info("Today's Lessons saved to message")
