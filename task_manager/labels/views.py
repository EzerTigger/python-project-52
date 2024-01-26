from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label

from django.utils.translation import gettext_lazy as _

from task_manager.users.mixins import LoginRequiredCustomMixin
from task_manager.labels.mixins import DeleteLabelProtectedMixin


class LabelsList(LoginRequiredCustomMixin, ListView):
    model = Label
    context_object_name = 'labels'
    permission_denied_message = _('You are not logged in. Please log in')


class CreateLabelView(LoginRequiredCustomMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/create_label.html'
    success_url = reverse_lazy('label_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Label successfully created')


class UpdateLabelView(LoginRequiredCustomMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/update_label.html"
    success_url = reverse_lazy('label_list')
    permission_denied_message = _('You are not logged in. Please log in')
    success_message = _('Label update successfully')


class DeleteLabelView(LoginRequiredCustomMixin, DeleteLabelProtectedMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('label_list')
    permission_denied_message = _('You are not logged in. Please log in')
    protected_error_message = _("Label can't be deleted - on use now")
    success_message = _('Label was deleted successfully')
