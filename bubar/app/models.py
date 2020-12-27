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


class OperatorHistory(models.Model):
    flow_type = models.CharField('流类型', max_length=10)

    project_name = models.CharField("项目名称", max_length=100)
    operator = models.CharField("操作员", max_length=100)
    page = models.CharField("Page", max_length=100, blank=True, null=True)
    fluid = models.CharField("Fluid", max_length=100, blank=True, null=True)
    tag_number = models.CharField("Tag Number", max_length=100, blank=True, null=True)
    operator = models.CharField("操作员", max_length=100)
    create_time = models.DateTimeField(auto_created=True)
