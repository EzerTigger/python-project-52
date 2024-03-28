from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

from task_manager.users.mixins import LoginRequiredCustomMixin


class CreateStatusView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Status successfully created')


class StatusesList(LoginRequiredCustomMixin, ListView):
    model = Status
    permission_denied_message = _('You are not logged in. Please log in')


class UpdateStatusView(LoginRequiredCustomMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = "statuses/status_update.html"
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Status update successfully')


class DeleteStatusView(LoginRequiredCustomMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('status_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Status deleted successfully')
