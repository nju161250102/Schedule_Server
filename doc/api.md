# 接口设计文档

### DDL提醒(/deadline)
* [POST]/: 新增DDL、新增提醒消息
* [UPDATE]/: 更新DDL、更新提醒消息时间
* [GET]/: 获取未到时间的DDL列表
* [DELETE]/: 删除DDL、删除提醒消息
* [GET]/{id}: 获取某条DDL（用于修改）

### 消息(/msg)
* [GET]/: 获取未读的消息列表
* [GET]/{id}: 获取某条消息（可能会用到）
* [UPDATE]/{id}/read_flag: 设置为已读
