from django import forms
from client.models import Client


class StyleFormMixin:
    """
    Стилизация форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():        
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """
    Форма модели Клиент
    """
    class Meta:
        """
        Методанные формы модели клиента
        """
        model = Client
        fields = (
            'last_name',
            'first_name',
            'surname',
            'email',
            'comment',
        )     
