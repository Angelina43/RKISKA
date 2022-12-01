from models import *
from django import forms
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    lastName = forms.CharField(label='Фамилия',
                                error_messages={
                                    'required': 'Обязательное поле',
                                }, )
    firstName = forms.CharField(label='Имя',
                                 error_messages={
                                     'required': 'Обязательное поле',
                                 })
    username = forms.CharField(label='Логин',
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин занят'
                               })
    password = forms.CharField(label='Пароль',
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    password2 = forms.CharField(label='Пароль (повторно)',
                                error_messages={
                                    'required': 'Обязательное поле',
                                })
    img = forms.ImageField(label='Фото')

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Пароли не совпадают', code='pass_error')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('lastName', 'firstName', 'username', 'password', 'password2', 'img')
        enctype = "multipart/form-data"
