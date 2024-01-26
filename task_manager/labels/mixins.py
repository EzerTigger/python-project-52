from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.views.generic.edit import DeletionMixin
from django.contrib import messages


class DeleteLabelProtectedMixin(DeletionMixin):
    protected_error_message = ''
    success_message = ''

    def form_valid(self, form):
        try:
            super().delete(self.request)
        except ProtectedError:
            messages.error(self.request, self.protected_error_message)
        else:
            messages.info(self.request, self.success_message)
        return redirect(self.get_success_url())
