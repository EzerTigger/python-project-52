from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статус'

    def __str__(self):
        return self.name
