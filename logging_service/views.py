from logging_service.models import LogMailing
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView


class LogMailingListView(ListView):
    model = LogMailing
    template_name = 'logging_service/logging_service_list.html'

class LogMailingDeleteView(DeleteView):
    model = LogMailing
    template_name = 'logging_service/logging_service_detail.html'
    success_url = reverse_lazy('logging_service:logging_services')


class LogMailingDetailView(DetailView):
    model = LogMailing
    template_name = 'logging_service/logging_service_confirm_delete.html'