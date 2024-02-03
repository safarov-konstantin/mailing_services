from django.urls import path
from client.apps import ClientConfig
from client.views import(
    ClientCreateView,
    ClientListView,
    ClientUpdateView,
    ClietnDeleteView,
    ClietnDetailView
)


app_name = ClientConfig.name


urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('', ClientListView.as_view(), name='clients'),
    path('detail_client/<int:pk>', ClietnDetailView.as_view(), name='detail_client'),
    path('edit_client/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('delite_client/<int:pk>/', ClietnDeleteView.as_view(), name='delite_client'),

]