from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy


class LoginRequiredCustomMixin:
    permission_denied_message = ''
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class UserCustomTestMixin(UserPassesTestMixin):
    modify_error_message = ''

    def test_func(self):
        user_instance = User.objects.get(pk=self.request.user.id)
        obj = self.get_object()
        object_instance = User.objects.get(pk=obj.id)
        return user_instance == object_instance

    def handle_no_permission(self):
        messages.error(self.request, self.modify_error_message)
        return redirect('users')
