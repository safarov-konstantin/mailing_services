from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import MassegeForm, MailingForm
from mailing.models import Message, Mailing
from client.models import Client
from blog.models import Page
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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data( **kwargs)
        context_data['count_mailings'] = Mailing.objects.all().count()
        context_data['count_mailings_is_active'] = Mailing.objects.filter(status=Mailing.Status.STARTED).count()
        context_data['clients_count'] = Client.objects.all().order_by('email').distinct('email').count()
        context_data['random_blog'] = Page.objects.order_by('?')[:3]
        return context_data


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания сообщения
    """
    model = Message
    form_class = MassegeForm
    success_url = reverse_lazy('mailing:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    """
    Контроллер для станицы сообщения
    """
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        _user = self.request.user
        if not _user.is_superuser:
            queryset = queryset.filter(owner=_user)   
        return queryset


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
        

class MailingListView(LoginRequiredMixin, ListView):
    """
    Контроллер для страницы рассылок
    """
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        _user = self.request.user
        if _user.is_superuser:
            queryset = super().get_queryset(*args, **kwargs)
        elif _user.groups.filter(name='managers'):
            queryset = super().get_queryset(*args, **kwargs)
        else:
            queryset = super().get_queryset(*args, **kwargs)
            queryset = queryset.filter(author=_user)
        return queryset


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
    