from django.db import models


NULLABLE = {'null': True, 'blank': True}


class LogMailing(models.Model):
    """
    Логирование рассылок
    """
    class Status(models.TextChoices):
        """
        Статусы логов сервиса рассылки
        """
        ERROR = 'error', 'ошибка'
        SUCCESS = 'success', 'успешно'

    time = models.DateField(auto_now_add=True, verbose_name='Время последеней попытки')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.SUCCESS, 
                              verbose_name='Статус попытки')
    server_response = models.CharField(max_length=150, verbose_name='Ответ сервера', **NULLABLE)
    mailing = models.ForeignKey('mailing.Mailing', on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        """
        Представление логов сервиса рассылки
        """
        return f'{self.time} {self.status} {self.mailing}'
    
    class Meta:
        """
        Методанные логов сервиса рассылки
        """
        verbose_name = 'Лог сервиса рассылок'
        verbose_name_plural = 'Логи сервиса рассылок'
        ordering =['-time']
        indexes = [
            models.Index(fields=['-time'])
        ]
