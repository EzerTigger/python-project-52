from django.db import models

from task_manager.tasks.models import Task


class Label(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    tasks = models.ManyToManyField(Task)
