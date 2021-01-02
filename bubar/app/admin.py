from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Factor, OperationHistory


class FactorAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'pipe_id_min', 'pipe_id_max', 'factor')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'create_time', 'project_name', 'operator',)

    list_filter = ('flow_type',)
    search_fields = ['project_name', "operator"]
    change_list_template = "admin/change_list.html"

    # def button(self, obj):
    #     return mark_safe('<input type="...">')
    # title.short_description = 'Action'
    # title.allow_tags = True


admin.site.register(OperationHistory, HistoryAdmin)

admin.site.register(Factor, FactorAdmin)
