import django_filters

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(label=_('Status'),
                                              queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(label=_('Executor'),
                                                queryset=User.objects.all())
    label = django_filters.ModelMultipleChoiceFilter(
        label=_('Label'),
        queryset=Label.objects.all()
    )
 
    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']

