from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, \
    DeleteView, UpdateView
from .forms import LoginUserForm, UserForm
from .mixins import UserCustomTestMixin, LoginRequiredCustomMixin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(CreateView):
    form_class = UserForm
    template_name = 'auth/user_form.html'
    success_url = reverse_lazy('login')


class UsersListView(ListView):
    model = User


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.info(self.request, _('Login successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Login Error'))
        return super().form_invalid(form)


def logout_user(request):
    logout(request)
    messages.info(request, _('Logout successfully'))
    return redirect('home')


class UpdateUserView(LoginRequiredCustomMixin, UserCustomTestMixin,
                     SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "auth/user_update_form.html"
    success_url = reverse_lazy('users')
    permission_denied_message = _('Please login to modify user')
    modify_error_message = _('You cannot edit another user')
    success_message = _('User update successfully')


class DeleteUserView(LoginRequiredCustomMixin, UserCustomTestMixin, DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('login')
    permission_denied_message = _('Please login to delete user')
    modify_error_message = _('You cannot delete another user')



