from rest_framework import serializers

from .models import User, Task

"""сериализатор - сердце DRF формирует данные для ответов на IP запросы, и выполняет парсинг входной информации 
отдает данные из БД либо добавляет редактирует или удаляет из БД"""


class RegistrationSerializer(serializers.ModelSerializer):
    """Получает данные из RegistrationViewSet обрабатывает входящие запросы и создает исходящие передавая их обратно в
    RegistrationViewSet. работает с моделью User"""
    print("Запустился RegistrationSerializer")

    class Meta:
        model = User
        fields = '__all__'

    print("Завершился RegistrationSerializer")


class TaskSerializer(serializers.ModelSerializer):
    """Получает данные из TaskViewSet обрабатывает входящие запросы и создает исходящие передавая их обратно в
    TaskViewSet. работает с моделью Task"""
    print("Запустился TaskSerializer")

    class Meta:
        model = Task
        fields = '__all__'

    print("Завершился TaskSerializer")
