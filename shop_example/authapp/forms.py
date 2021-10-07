from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field-form'
            field.widget.attrs['placeholder'] = field.label
            field.label = ''


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field-form'
            if field_name != 'avatar' and field_name != 'age':
                field.widget.attrs['placeholder'] = field.label
                field.label = ''
            field.help_text = ''


class UserEditForm(UserChangeForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field-form'
            if field_name != 'avatar' and field_name != 'age':
                field.widget.attrs['placeholder'] = field.label
                # field.label = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
            field.help_text = ''
