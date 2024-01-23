from django.db import models
from django.contrib.auth.models import User


from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='tasks', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='created_tasks')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'

    def __str__(self):
        return self.name
