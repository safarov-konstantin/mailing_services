from django.urls import path
from logging_service.apps import LoggingServiceConfig
from logging_service.views import LogMailingDeleteView, LogMailingDetailView, LogMailingListView


app_name = LoggingServiceConfig.name


urlpatterns = [
    path('', LogMailingListView.as_view(), name='logging_services'),
    path('detail_logging_service/<int:pk>/', LogMailingDetailView.as_view(), name='detail_logging_service'),
    path('delite_logging_service/<int:pk>/', LogMailingDeleteView.as_view(), name='delite_logging_service'),    
]
