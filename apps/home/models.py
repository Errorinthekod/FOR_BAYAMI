from django.db import models

from django.db import models

# Create your models here.

# Create your models here.


class About(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')

class Contact(models.Model):
    name = models.CharField('Имя', max_length=200)
    email = models.CharField('Почта', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    subject = models.CharField('Субъект', max_length=200)
    message = models.CharField('Сообщение', max_length=200)