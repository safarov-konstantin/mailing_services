from client.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from client.forms import ClientForm
from django.urls import reverse_lazy
from django.views.generic import ( 
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')

    def form_valid(self, form) :
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        _user = self.request.user
        if not _user.is_superuser:
            queryset = queryset.filter(owner=_user)   
        return queryset


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')

    def test_func(self):
        _user = self.request.user
        if _user.is_superuser:
            return True
        elif self.owner == _user:
            return True
        else:
            return self.handle_no_permission()


class ClietnDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:clients')

    def test_func(self):
        _user = self.request.user
        if _user.is_superuser:
            return True
        elif self.get_object().owner == _user:
            return True
        else:
            return self.handle_no_permission()


class ClietnDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def test_func(self):
        _user = self.request.user
        if _user.is_superuser:
            return True
        elif self.get_object().owner == _user:
            return True
        else:
            return self.handle_no_permission()
