from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(blank=False, null=False,max_length=40)
    email = models.EmailField(unique=True, max_length=100)


class Naver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    birthdate = models.DateField()
    admission_date = models.DateField()

    class Meta:
        verbose_name = 'Naver'
        verbose_name_plural = 'Navers'
        db_table = 'navers'

    def __str__(self):
        return f'Naver: {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'Project: {self.name}'
