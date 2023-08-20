from rest_framework import serializers

from .models import User, Task


class RegistrationSerializer(serializers.ModelSerializer):
    print("Запустился RegistrationSerializer")

    class Meta:
        model = User
        fields = '__all__'

    print("Завершился RegistrationSerializer")


class TaskSerializer(serializers.ModelSerializer):
    print("Запустился TaskSerializer")
    # status = serializers.CharField(source='status.name')

    class Meta:
        model = Task
        fields = '__all__'

    print("Завершился TaskSerializer")

    # def create(self, validated_data):
    #     return Task(**validated_data)



