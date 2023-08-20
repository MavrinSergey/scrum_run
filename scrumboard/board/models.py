from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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


class Task(models.Model):
    print("Запустился Task")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_creation = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20)
    lead_time = models.DateField()
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    print("Завершился Task")
