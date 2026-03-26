from django.contrib import admin
from .models import RepairRequest

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'phone', 'vehicle', 'urgency', 'status', 'timestamp']
    list_filter   = ['status', 'urgency', 'vehicle']
    search_fields = ['name', 'phone', 'vehicle']
    ordering      = ['-timestamp']

