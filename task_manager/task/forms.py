from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]

        # labels = {}

        # widgets = {
        #     'password': forms.PasswordInput(),
        # }


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user
