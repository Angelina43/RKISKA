import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    username = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    firstName = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    lastName = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    img = models.ImageField(max_length=254, blank=True, null=False)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName) + '(' + str(self.username) + ')'
