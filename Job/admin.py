from django.contrib import admin
from .models import Job

# Register your models here.

# admin.site.register(Job)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_location')
    list_filter = ('category',)
    search_fields = ('job_title',)
    ordering = ('id',)