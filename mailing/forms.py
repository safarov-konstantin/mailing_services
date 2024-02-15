from django import forms
from mailing.models import Message, Mailing
from client.models import Client


class StyleFormMixin:
    """
    Стилизация форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():        
            field.widget.attrs['class'] = 'form-control'


class MassegeForm(StyleFormMixin, forms.ModelForm):
    """
    Форма модели сообщение
    """
    class Meta:
        """
        Методанные формы модели сообщения
        """
        model = Message
        fields = [
            'title',
            'body',
        ]


class MailingForm(StyleFormMixin, forms.ModelForm):
    """
    Форма модели рассылки
    """

    def __init__(self, *args, **kwargs):
        _user = kwargs['user']
        del kwargs['user']
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(owner=_user)
        self.fields['message'].queryset = Message.objects.filter(owner=_user)

    class Meta:
        """
        Методанные формы модели сообщения
        """
        model = Mailing
        fields = [
            'time',
            'date',
            'periodisity',
            'status',
            'client',
            'message',
        ]
        