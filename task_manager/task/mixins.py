from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


class UserCustomTestMixin(UserPassesTestMixin):
    def test_func(self):
        user_instance = User.objects.get(pk=self.request.user.id)
        obj = self.get_object()
        object_instance = User.objects.get(pk=obj.id)
        return user_instance == object_instance

    def handle_no_permission(self):
        messages.error(self.request, "Noooo!")
        return redirect('users')
