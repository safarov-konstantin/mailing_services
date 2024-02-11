from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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


class HomePageTemplateView(LoginRequiredMixin, TemplateView):
    """
    Контроллер для домашней страницы
    """
    template_name = 'mailing/dashboard.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания сообщения
    """
    model = Message
    form_class = MassegeForm
    success_url = reverse_lazy('mailing:messages')


class MessageListView(LoginRequiredMixin, ListView):
    """
    Контроллер для станицы сообщения
    """
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления сообщения
    """
    model = Message
    form_class = MassegeForm
    success_url = reverse_lazy('mailing:messages')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления сообщения
    """
    model = Message
    success_url = reverse_lazy('mailing:messages')


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра сообщения
    """
    model = Message


class MailingCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания рассылки
    """
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')


class MailingListView(LoginRequiredMixin, ListView):
    """
    Контроллер для страницы рассылок
    """
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления рассылки
    """
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления рассылки
    """
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')


class MailingDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра рассылки
    """
    model = Mailing
    