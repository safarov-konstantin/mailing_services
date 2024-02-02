from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import HomePageTemplateView


app_name = MailingConfig.name


urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page')
]
