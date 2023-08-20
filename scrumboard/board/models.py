import jwt
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    """User model."""
    print("Запустился User")
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    print("Завершился User")


class SignIn(models.Model):
    print("Запустился SignIn")
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    signin_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    print("Завершился SignIn")

class StatusTask(models.Model):
    print("Запустился StatusTask")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    print("Завершился StatusTask")


class Project(models.Model):
    print("Запустился Project")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_creation = models.DateField(auto_now_add=True)
    date_expiration = models.DateField()

    def __str__(self):
        return self.title

    print("Завершился Project")


class Company(models.Model):
    print("Запустился Company")
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    print("Завершился Company")


class StatusUserProjects(models.Model):
    print("Запустился StatusUserProjects")
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    print("Завершился StatusUserProjects")

class ProjectParticipants(models.Model):
    """

    """
    print("Запустился ProjectParticipants")
    project = models.ManyToManyField(Project, default='')
    user = models.ManyToManyField(User)
    status_user_project = models.ManyToManyField(StatusUserProjects)

    # def __str__(self):
    #     return self.project
    print("Завершился ProjectParticipants")

class Task(models.Model):
    print("Запустился Task")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_creation = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.ForeignKey(StatusTask, on_delete=models.PROTECT, null=True)
    lead_time = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    # id_project = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    print("Завершился Task")
