from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.forms import TaskForm
from task_manager.users.mixins import LoginRequiredCustomMixin


class CreateTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    #success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task successfully created')