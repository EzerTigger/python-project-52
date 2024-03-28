from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Метки'
        verbose_name = 'Метка'

    def __str__(self):
        return self.name
