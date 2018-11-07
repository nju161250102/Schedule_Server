# 数据库设计文档

### DDL表

|字段|类型|备注|
|:---|:---|:---|
|id|INT|主键、自增|
|time|TIMESTAMP|截止时间|
|title|VARCHAR(30)|标题|
|detail|VARCHAR(150)|详细描述|
|create_time|TIMESTAMP|创建时间（默认当前时间）|
|finish_time|TIMESTAMP|完成时间（未完成为null）|
|week_flag|INT|周提醒消息Id（未设定为null）|
|three_days_flag|INT|三天提醒消息Id（未设定为null）|
|day_flag|INT|日提醒消息Id（未设定为null）|

### 消息表

|字段|类型|备注|
|:---|:---|:---|
|id|INT|主键、自增|
|content|VARCHAR(150)|消息内容|
|time|TIMESTAMP|消息时间|
|read_flag|BOOLEAN|是否已读|
