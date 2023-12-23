from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UserChangeForm
from .models import *


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия'
        }))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
        }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Подтверждение пароля'
        }))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
        }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        }))
