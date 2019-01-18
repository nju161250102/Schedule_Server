# coding=utf-8
import time
from model import Plan


class PlanService(object):

    FINISHED = 0
    DELETED = -1
    PRIORITY_MAX = 5

    @staticmethod
    def add_plan(text, priority):
        if priority < 0 or priority > 5:
            priority = 1
        plan = Plan(text, priority)
        return plan.save()

    @staticmethod
    def finish_plan(plan_id):
        plan = Plan.get_by_id(plan_id)
        if plan is None:
            return 0
        plan.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        plan.flag = PlanService.FINISHED
        return plan.save()

    @staticmethod
    def delete_plan(plan_id):
        plan = Plan.get_by_id(plan_id)
        if plan is None:
            return 0
        plan.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        plan.flag = PlanService.DELETED
        return plan.save()

    @staticmethod
    def todo_list():
        result = Plan.select().where(Plan.flag > 0, Plan.flag <= PlanService.PRIORITY_MAX).order_by(Plan.flag.desc())
        return list(result.dicts())
