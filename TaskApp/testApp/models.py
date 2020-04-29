from django.db import models
class TaskModel(models.Model):
    tittle=models.CharField(max_length=50)
    status=models.CharField(max_length=40)
