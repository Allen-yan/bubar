import json

from django.db import models

FLOW_TYPE = (
    (1, '气体'),
    (2, '液体'),
    (3, '蒸汽'),
)


class Factor(models.Model):
    flow_type = models.CharField('流类型', max_length=10)
    pipe_id_min = models.DecimalField('D管道内径最小值', max_digits=7, decimal_places=3)
    pipe_id_max = models.DecimalField('D管道内径最大值', max_digits=7, decimal_places=3)
    factor = models.DecimalField('F系数', max_digits=12, decimal_places=5)

    class Meta:
        verbose_name = 'F系数'
        verbose_name_plural = 'F系数'


class OperationHistory(models.Model):
    flow_type = models.CharField('流类型', max_length=10)

    project_name = models.CharField("项目名称", max_length=100)
    operator = models.CharField("操作员", max_length=100)
    data = models.TextField("操作数据", default={})
    result = models.TextField("结果", default={})
    create_time = models.DateTimeField("操作时间", auto_now_add=True)

    class Meta:
        verbose_name = '操作历史'
        verbose_name_plural = '操作历史'


def log_history(flow_type, project_name, operator, data, result):
    oh = OperationHistory()
    oh.flow_type = flow_type
    oh.project_name = project_name
    oh.operator = operator
    oh.data = json.dumps(data)
    oh.result = json.dumps(result)
    oh.save()

    return oh
