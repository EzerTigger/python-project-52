from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from task_manager.statuses.forms import StatusForm


class CreateStatusView(CreateView):
    form_class = StatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('home')
