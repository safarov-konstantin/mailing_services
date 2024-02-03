from django import forms
from mailing.models import Message, Mailing


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