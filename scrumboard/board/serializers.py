from rest_framework import serializers

from .models import User, Task

"""сериализатор - сердце DRF формирует данные для ответов на IP запросы, и выполняет парсинг входной информации 
отдает данные из БД либо добавляет редактирует или удаляет из БД"""


class RegistrationSerializer(serializers.ModelSerializer):
    """Получает данные из RegistrationViewSet обрабатывает входящие запросы и создает исходящие передавая их обратно в
    RegistrationViewSet. работает с моделью User"""
    print("Запустился RegistrationSerializer")

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Хеширование пароля
        user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'email']
    print("Завершился RegistrationSerializer")


class TaskSerializer(serializers.ModelSerializer):
    """Получает данные из TaskViewSet обрабатывает входящие запросы и создает исходящие передавая их обратно в
    TaskViewSet. работает с моделью Task"""
    user_first_name = serializers.CharField(source='user.first_name', required=False)
    user_last_name = serializers.CharField(source='user.last_name', required=False)

    class Meta:
        model = Task
        fields = '__all__'
