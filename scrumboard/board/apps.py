from django.apps import AppConfig


class BoardConfig(AppConfig):
    """Запускает приложение board"""
    print("Запустился BoardConfig")
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
    print("Завершился BoardConfig")