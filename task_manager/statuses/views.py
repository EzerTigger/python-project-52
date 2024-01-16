from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

from task_manager.users.mixins import LoginRequiredCustomMixin


class CreateStatusView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Status successfully created')


class StatusesList(LoginRequiredCustomMixin, ListView):
    model = Status
    permission_denied_message = _('You are not logged in. Please log in')


class UpdateStatusView(LoginRequiredCustomMixin, SuccessMessageMixin, UpdateView):

    model = Status
    form_class = StatusForm
    template_name = "statuses/status_update.html"
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Status update successfully')


class DeleteStatusView(LoginRequiredCustomMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
