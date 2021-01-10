from django.contrib import admin
from django.utils.html import format_html

from .models import Factor, OperationHistory


class FactorAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'pipe_id_min', 'pipe_id_max', 'factor')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'flow_type', 'create_time', 'project_name', 'operator', 'buttons')

    list_filter = ('flow_type',)
    search_fields = ['project_name', "operator"]

    def buttons(self, obj):
        button_html = """<a class="button" href="/bubar/{}?id={}">重现</a>""".format(obj.flow_type, obj.id)
        return format_html(button_html)

    buttons.short_description = "操作"


admin.site.register(OperationHistory, HistoryAdmin)

admin.site.register(Factor, FactorAdmin)
