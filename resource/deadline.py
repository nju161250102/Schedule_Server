# coding=utf-8
import json
from flask import Blueprint
from flask import request
from service.deadline import DeadlineService

deadlineModule = Blueprint("deadline", __name__)
deadlineService = DeadlineService()


@deadlineModule.route("/", methods=["POST"])
def add_deadline():
    """ 新增一条DDL
    Request: {
        time: 时间,
        title: 标题,
        content: 内容,
        week_flag: 周提醒标记,
        three_days_flag: 三日提醒标记,
        day_flag: 前一日提醒标记
    }
    Responce：{
        type: success/error,
        *message: 出错详细信息
    }
    """
    req = request.get_json()
    add_result = deadlineService.add(req)
    return json.dumps({"type": "success" if add_result > 0 else "error"})


@deadlineModule.route("/<int:ddl_id>", methods=["PUT"])
def update_deadline(ddl_id):
    req = request.get_json()
    deadlineService.update(ddl_id, req)


@deadlineModule.route("/", methods=["GET"])
def get_deadline_list():
    req_type = request.args.get("type")
    deadline_dicts = deadlineService.get_list(req_type)
    return json.dumps([deadline for deadline in deadline_dicts], ensure_ascii=False)
