from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class StyleFormMixin:
    """
    Стилизация форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():        
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, UserCreationForm):
    """
    Форма входа пользователя
    """
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class RecoveryForm(StyleFormMixin, forms.Form):
    """
    Форма для востановления входа
    """
    email = forms.EmailField(label='Email')


class ProfileForm(StyleFormMixin, UserChangeForm):
    """
    Форма для профиля пользователя
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = (
            'email', 
            'first_name', 
            'last_name', 
        )
         
