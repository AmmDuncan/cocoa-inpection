from django.contrib import admin

from .models import Manager, Report

# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'make']
    
@admin.register(Manager)
class Manager(admin.ModelAdmin):
    list_display = ['name']