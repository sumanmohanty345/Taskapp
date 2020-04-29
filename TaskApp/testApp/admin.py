from django.contrib import admin
from testApp.models import TaskModel
class TaskShow(admin.ModelAdmin):
    list_display = ['tittle','status']

admin.site.register(TaskModel,TaskShow)
