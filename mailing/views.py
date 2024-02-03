from django.urls import reverse_lazy
from mailing.forms import MassegeForm
from mailing.models import Message
from django.views.generic import (
    TemplateView, 
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)


class HomePageTemplateView(TemplateView):
    template_name = 'mailing/dashboard.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MassegeForm
    success_url = reverse_lazy('mailing:messages')


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MassegeForm
    success_url = reverse_lazy('mailing:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')


class MessageDetailView(DetailView):
    model = Message