from django.core.mail import send_mail
from mailing.models import Mailing
from logging_service.models import LogMailing
from datetime import datetime, timedelta
from calendar import monthrange
from config.settings import EMAIL_HOST_USER
from smtplib import SMTPException


def send_mailing():
    """
    Отравка письма по условиям:
    time меньше или равно текущего времени
    date меньше или равно текущего времени
    status Запущена
    """
    current_time = datetime.now()
    mailings = Mailing.objects.filter(
        date__lte=current_time, 
        time__lte=current_time, 
        status='started'
    )

    for mailing in mailings:
        clients = mailing.client.all()
        message = mailing.message
        email_clients = [client.email for client in clients]
        try:
            response = send_mail(
                message.title,
                message.body,
                EMAIL_HOST_USER,
                email_clients
            )

            if bool(response):
                status_log = 'success'
                server_response = 'ОК'
            else:
                status_log = 'error'
                server_response = 'Ошибка'     

            log = LogMailing.objects.create(
                time=current_time,
                status=status_log,
                server_response=server_response,
                mailing=mailing
            )

            if mailing.periodisity == 'day':
                mailing.date += timedelta(days=1)
            elif mailing.periodisity == 'week':
                mailing.date += timedelta(weeks=1)
            elif mailing.periodisity == 'month':
                month = current_time.month
                year = current_time.year
                days_count = monthrange(year, month)
                mailing.date += timedelta(days=days_count[1])
                mailing.save()
                log.save()
        
        except SMTPException as e:

            log = LogMailing.objects.create(
                time=current_time,
                status='error',
                server_response=e,
                mailing=mailing
            )
            log.save()

        except Exception as e:

            log = LogMailing.objects.create(
                time=current_time,
                status='error',
                server_response=e,
                mailing=mailing
            )
            log.save()
            
