# coding=utf-8
import time
from datetime import datetime
from model import Term, Lesson


class LessonService(object):

    @staticmethod
    def get_lessons():
        now_date = time.strftime("%Y-%m-%d", time.localtime())
        term = Term.get((Term.start <= now_date) & (now_date <= Term.end))
        day_num = (datetime.now() - datetime.strptime(term.start, "%Y-%m-%d")).days
        week_flag = int((day_num / 7) + 1) % 2  # 0 is double week
        weekday = int(time.strftime("%w", time.localtime()))
        result = Lesson.select().where(Lesson.term == term.id,
                                       Lesson.week == week_flag,
                                       Lesson.weekday == weekday)
        return list(result.dicts())
