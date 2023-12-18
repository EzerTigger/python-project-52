from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .forms import CreateUserForm
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(CreateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'username',
        'password'
    ]


