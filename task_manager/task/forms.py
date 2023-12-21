from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class CreateUserForm(UserCreationForm):
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


class UpdateUserForm(forms.ModelForm):

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
