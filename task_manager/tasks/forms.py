from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'executor',
            'labels'
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name'),
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description'),
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': Status,
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': User,
                }
            ),
            'labels': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'choices': Label,
                }
            )
        }
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels')
        }
