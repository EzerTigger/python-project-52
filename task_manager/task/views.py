from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, \
    DeleteView, UpdateView
from .forms import CreateUserForm, LoginUserForm, UpdateUserForm
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('home')


class UsersListView(ListView):
    model = User


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class UpdateUserView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('users')


class DeleteUserView(DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('login')



