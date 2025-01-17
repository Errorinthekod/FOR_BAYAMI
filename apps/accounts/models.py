from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager



class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    GENDER_CHOICE = [('male', 'male'),
                         ('female', 'female')]
    username = models.CharField('Никнейм', max_length=255, unique= True)
    email = models.EmailField('Почта',  max_length=255, unique= True)
    avatar = models.ImageField('Аватарка', upload_to = 'users/', blank = True, null = True)
    about = models.TextField('О себе', blank = True, null = True)
    birth_date = models.DateField('Дата рождения', blank = True, null = True)
    phone = models.CharField('Телефон',max_length=25, unique= True, blank = True, null = True)
    city = models.CharField('Город', max_length=100, unique= True, blank = True, null = True)
    gender = models.CharField('Пол', choices = GENDER_CHOICE, default = 'male', blank = True, null = True)


    objects = UserManager()
    def __str__(self):
        return self.username