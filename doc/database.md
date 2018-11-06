# 数据库设计文档

### DDL表

|字段|类型|备注|
|:---|:---|:---|
|id|INT|主键、自增|
|time|TIMESTAMP|截止时间|
|title|VARCHAR(30)|标题|
|detail|VARCHAR(150)|详细描述|
|create_time|TIMESTAMP|创建时间|
|finish_time|TIMESTAMP|完成时间（未完成为null）|
|week_flag|BOOLEAN|周提醒设置标记|
|three_days_flag|BOOLEAN|三天提醒设置标记|
|day_flag|BOOLEAN|日提醒设置标记|

### 消息表

|字段|类型|备注|
|:---|:---|:---|
|id|INT|主键、自增|
|content|VARCHAR(150)|消息内容|
|time|TIMESTAMP|消息生成时间|
|read_flag|BOOLEAN|是否已读|
