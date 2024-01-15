from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class CreateStatusView(CreateView):
    form_class = StatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('home')


class StatusesList(ListView):
    model = Status
