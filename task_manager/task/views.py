from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import CreateUserForm
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(FormView):
    template_name = 'create_user.html'
    form_class = CreateUserForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        User.objects.create(**form.cleaned_data)
        return super().form_valid(form)
