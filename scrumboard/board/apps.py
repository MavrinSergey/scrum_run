from django.apps import AppConfig


class BoardConfig(AppConfig):
    """Запускает приложение board"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
