from django.contrib import admin

from .models import Factor


class FactorAdmin(admin.ModelAdmin):
    list_display = ('flow_type', 'pipe_id_min', 'pipe_id_max', 'factor')


admin.site.register(Factor, FactorAdmin)
