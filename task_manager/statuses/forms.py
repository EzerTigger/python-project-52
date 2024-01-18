from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Name')
        }))

    class Meta:
        model = Status
        fields = [
            'name',
        ]
