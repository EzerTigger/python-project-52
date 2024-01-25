from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Метки'
        verbose_name = 'Метка'

    def __str__(self):
        return self.name
