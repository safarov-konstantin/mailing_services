from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (
    HomePageTemplateView,
    # massages
    MessageListView,
    MessageCreateView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
    # mailings
    MailingCreateView,
    MailingListView,
    MailingDetailView,
    MailingUpdateView,
    MailingDeleteView
)


app_name = MailingConfig.name


urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    # mailings
    path('mailings/create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('mailings/detail_mailing/<int:pk>/', MailingDetailView.as_view(), name='detail_mailing'),
    path('mailings/edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
    path('mailings/delite_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delite_mailing'),
    # massages
    path('massages/create_client/', MessageCreateView.as_view(), name='create_message'),
    path('massages/', MessageListView.as_view(), name='messages'),
    path('massages/detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('massages/edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('massages/delite_message/<int:pk>/', MessageDeleteView.as_view(), name='delite_message'),
]
