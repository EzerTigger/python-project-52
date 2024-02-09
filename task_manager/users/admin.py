from django.contrib import admin
from django.contrib.auth.models import User


def get_full_name(self):
    return self.first_name + ' ' + self.last_name


User.__str__ = get_full_name



