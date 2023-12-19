from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'confirm_password'
        ]

        labels = {}

        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit and self.cleaned_data['password'] == \
                self.cleaned_data['confirm_password']:
            user.save()
        return user
