import jwt
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class SignIn(models.Model):
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    signin_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class StatusTask(models.Model):
    """

    """
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_creation = models.DateField(auto_now_add=True)
    date_expiration = models.DateField()

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StatusUserProjects(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ProjectParticipants(models.Model):
    """

    """
    project = models.ManyToManyField(Project, default='')
    user = models.ManyToManyField(User)
    status_user_project = models.ManyToManyField(StatusUserProjects)

    # def __str__(self):
    #     return self.project


class Task(models.Model):
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
