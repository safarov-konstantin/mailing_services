from logging_service.models import LogMailing
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView


class LogMailingListView(LoginRequiredMixin, ListView):
    """
    Контроллер вывода логов рассылки(Листа логов)
    """
    model = LogMailing
    template_name = 'logging_service/logging_service_list.html'

class LogMailingDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления логов рассылки
    """
    model = LogMailing
    template_name = 'logging_service/logging_service_confirm_delete.html'
    success_url = reverse_lazy('logging_service:logging_services')


class LogMailingDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра лога
    """
    model = LogMailing
    template_name = 'logging_service/logging_service_detail.html'
    