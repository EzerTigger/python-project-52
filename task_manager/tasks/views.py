from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib import messages
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.users.mixins import LoginRequiredCustomMixin
from task_manager.tasks.filters import TaskFilter


class CreateTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksList(LoginRequiredCustomMixin, ListView):
    model = Task
    permission_denied_message = _('You are not logged in. Please log in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TaskDetail(LoginRequiredCustomMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = self.object.labels.all()
        return context


class UpdateTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task update successfully')


class DeleteTaskView(LoginRequiredCustomMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
