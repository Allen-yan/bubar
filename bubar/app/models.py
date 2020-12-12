from django.db import models

FLOW_TYPE = (
    (1, '气体'),
    (1, '液体'),
    (1, '蒸汽'),
)


class Factor(models.Model):
    flow_type = models.SmallIntegerField('流类型', choices=FLOW_TYPE)
    pipe_id_min = models.DecimalField('D管道内径最小值', max_digits=7, decimal_places=3)
    pipe_id_max = models.DecimalField('D管道内径最大值', max_digits=7, decimal_places=3)
    factor = models.DecimalField('F系数', max_digits=12, decimal_places=5)


    class Meta:
        verbose_name = 'F系数'
        verbose_name_plural = 'F系数'
"Insert into factor (factor, flow_type, pipe_id_min, pipe_id_max) values()"