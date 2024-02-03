from client.models import Client
from client.forms import ClientForm
from django.urls import reverse_lazy
from django.views.generic import ( 
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:clients')


class ClietnDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:clients')


class ClietnDetailView(DetailView):
    model = Client
