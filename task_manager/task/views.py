from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, \
    DeleteView, UpdateView
from .forms import LoginUserForm, UserForm
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(CreateView):
    form_class = UserForm
    template_name = 'auth/user_form.html'
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


class UpdateUserView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "auth/user_update_form.html"
    success_url = reverse_lazy('users')

    def test_func(self):
        user_instance = User.objects.get(pk=self.request.user.id)
        obj = self.get_object()
        object_instance = User.objects.get(pk=obj.id)
        return user_instance == object_instance

    def handle_no_permission(self):
        # здесь, по идее, flash
        return redirect('users')


class DeleteUserView(DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('login')



