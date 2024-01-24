from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages
from task_manager.labels.models import Label

from django.utils.translation import gettext_lazy as _

from task_manager.users.mixins import LoginRequiredCustomMixin


class LabelsList(LoginRequiredCustomMixin, ListView):
    model = Label
    permission_denied_message = _('You are not logged in. Please log in')