from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (
    HomePageTemplateView,
    MessageListView,
    MessageCreateView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
    )


app_name = MailingConfig.name


urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('massages/create_client/', MessageCreateView.as_view(), name='create_message'),
    path('massages/', MessageListView.as_view(), name='messages'),
    path('massages/detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('massages/edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('massages/delite_message/<int:pk>/', MessageDeleteView.as_view(), name='delite_message'),
]
