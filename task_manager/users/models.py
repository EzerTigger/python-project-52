from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статус'

    def __str__(self):
        return self.name

