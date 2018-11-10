# coding=utf-8
import datetime
import json
from flask import Blueprint
from flask import request
from model.deadline import Deadline
from model.message import Message

deadlineModule = Blueprint("deadline", __name__)


@deadlineModule.route("/", methods=["POST"])
def add_deadline():
    req = request.get_json()
    time = datetime.datetime.strptime(req["time"], "%Y-%m-%d %H:%M:%S")
    # 保存提醒消息
    text_dict = {
        "week_flag": "一星期",
        "three_days_flag": "三天",
        "day_flag": "最后一天"
    }
    time_dict = {
        "week_flag": (time - datetime.timedelta(7)).strftime("%Y-%m-%d %H:%M:%S"),
        "three_days_flag": (time - datetime.timedelta(3)).strftime("%Y-%m-%d %H:%M:%S"),
        "day_flag": (time - datetime.timedelta(1)).strftime("%Y-%m-%d %H:%M:%S"),
    }
    for key in ["week_flag", "three_days_flag", "day_flag"]:
        if req[key]:
            msg = Message("[提醒]距离DDL：%s 到期还有%s" % (req["title"], text_dict[key]),
                          time_dict[key])
            msg.save()
            req[key] = msg.id
    # 保存deadline对象
    deadline = Deadline(
        time=req["time"],
        title=req["title"],
        detail=req["detail"],
        week_flag=req["week_flag"],
        three_days_flag=req["three_days_flag"],
        day_flag=req["day_flag"]
    )
    line = deadline.save()
    return "sucess"


@deadlineModule.route("/", methods=["GET"])
def get_deadline_list():
    req_type = request.args.get("type")
    deadline_dicts = {}
    if req_type == "all":
        deadline_dicts = Deadline.select().dicts()
    elif req_type == "active":
        deadline_dicts = Deadline.select().where(Deadline.finish_time is not None).dicts()
    return json.dumps([deadline for deadline in deadline_dicts], ensure_ascii=False)
