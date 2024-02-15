from django.db import models
from users.models import User


NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    """
    Модель сообщение
    """
    title = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        """
        Представление сообщения
        """
        return self.title

    class Meta:
        """
        Методанные сообщения
        """
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('title',)


class Mailing(models.Model):
    """
    Модель Рассылка
    """
    class Status(models.TextChoices):
        """
        Статусы рассылок
        """
        CREATED = 'created', 'Создана'
        STARTED = 'started', 'Запущена'
        COMPLETED = 'completed', 'Завершена'

    class Periodicity(models.TextChoices):
        """
        Варианты переодичности рассылок
        """
        DAY = 'day', 'Раз в день'
        WEEK = 'week', 'Раз в неделю'
        MONTH = 'month', 'Раз в месяц'    

    time = models.TimeField(verbose_name='Время рассылки')
    date = models.DateField(verbose_name='Дата рассылки')
    periodisity = models.CharField(max_length=20, choices=Periodicity.choices, default=Periodicity.MONTH,
                                   verbose_name='Периодичность')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CREATED, 
                              verbose_name='Статус рассылки')
    client = models.ManyToManyField('client.Client', verbose_name='Клиент')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Сообщение')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', **NULLABLE)

    def __str__(self):
        """
        Представление рассылок
        """
        performance = (
            f'Дата: {self.date} \n'
            + 'Сообщение:'
            + f'{self.message}'
        )
        return performance

    class Meta:
        """
        Методанные рассылок
        """
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
