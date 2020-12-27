from django.contrib import admin

from .models import Factor, OperationHistory


class FactorAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'pipe_id_min', 'pipe_id_max', 'factor')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'create_time', 'project_name', 'operator')

    list_filter = ('flow_type',)
    search_fields = ['project_name', "operator"]


admin.site.register(OperationHistory, HistoryAdmin)

admin.site.register(Factor, FactorAdmin)
