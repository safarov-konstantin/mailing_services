from django.urls import reverse_lazy
from mailing.forms import MassegeForm, MailingForm
from mailing.models import Message, Mailing
from django.views.generic import(
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


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')


class MailingListView(ListView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')


class MailingDetailView(DetailView):
    model = Mailing