from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """
    Модель клиент
    """
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    surname = models.CharField(max_length=150, verbose_name='отчетство')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        """
        Представление клиента
        """
        return f'{self.last_name} {self.first_name} {self.surname} ({self.email})'
    
    class Meta:
        """
        Методанные модели клиент
        """
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
