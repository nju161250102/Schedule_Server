# coding=utf-8
import time
from model import Plan


class PlanService(object):

    FINISHED = 0
    DELETED = -1
    PRIORITY_MAX = 5

    @staticmethod
    def add(text, priority):
        plan = Plan()
        plan.detail = text
        plan.flag = priority
        if priority == PlanService.FINISHED:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            plan.time = now_time
            plan.create_time = now_time
        else:
            if priority < 0 or priority > PlanService.PRIORITY_MAX:
                plan.flag = 1
        return plan.get_id() if plan.save() != 0 else 0

    @staticmethod
    def update(plan_id, flag):
        plan = Plan.get_or_none(Plan.id == plan_id)
        if plan is None:
            return False
        plan.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        plan.flag = flag
        return plan.save() != 0

    @staticmethod
    def finish(plan_id):
        return PlanService.update(plan_id, PlanService.FINISHED)

    @staticmethod
    def delete(plan_id):
        return PlanService.update(plan_id, PlanService.DELETED)

    @staticmethod
    def todo_list():
        result = Plan.select().where(Plan.flag > 0, Plan.flag <= PlanService.PRIORITY_MAX).order_by(Plan.flag.desc())
        return list(result.dicts())
