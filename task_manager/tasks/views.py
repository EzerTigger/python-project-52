from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from task_manager.tasks.models import Task
from task_manager.users.mixins import LoginRequiredCustomMixin
from task_manager.tasks.filters import TaskFilter


class CreateTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task successfully created')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = _('Name')
        form.fields['description'].label = _('Description')
        form.fields['status'].label = _('Status')
        form.fields['executor'].label = _('Executor')
        form.fields['labels'].label = _('Labels')
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksList(LoginRequiredCustomMixin, FilterView):
    model = Task
    permission_denied_message = _('You are not logged in. Please log in')
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        if self.request.GET.get('own') == 'on':
            user = self.request.user
            return Task.objects.filter(author=user)
        else:
            return Task.objects.all()


class TaskDetail(LoginRequiredCustomMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = self.object.labels.all()
        return context


class UpdateTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task update successfully')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = _('Name')
        form.fields['description'].label = _('Description')
        form.fields['status'].label = _('Status')
        form.fields['executor'].label = _('Executor')
        form.fields['labels'].label = _('Labels')
        return form


class DeleteTaskView(LoginRequiredCustomMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Task deleted successfully')
