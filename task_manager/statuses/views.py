from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib import messages
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

from task_manager.users.mixins import LoginRequiredCustomMixin


class CreateStatusView(CreateView, SuccessMessageMixin):
    form_class = StatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, _('Status successfully created'))
        return super().form_valid(form)


class StatusesList(LoginRequiredCustomMixin, ListView):
    model = Status
    permission_denied_message = _('You are not logged in. Please log in')
