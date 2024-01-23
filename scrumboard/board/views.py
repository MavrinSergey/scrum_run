from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Task, User
from .serializers import RegistrationSerializer, TaskSerializer

"""представления создаются средствами DRF
    задача представлений обработка запроса и отправка данных пользователю
    задача по формированию запроса передается Сериализаторам"""


class RegistrationViewSet(generics.ListCreateAPIView):
    """класс для обработки запроcов к модели User"""

    print("Запустился RegistrationViewSet")
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    print("Завершился RegistrationViewSet")


class TaskViewSet(viewsets.ModelViewSet):
    """класс для обработки запроcов к модели Task"""

    print("Запустился TaskViewSet")
    queryset = Task.objects.all().select_related('user')
    serializer_class = TaskSerializer
    print("Завершился TaskViewSet")

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return TaskSerializer

        return self.serializer_class


def index(request):
    return render(request, 'index.html')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer): # Создаем пользовательский ответ на запрос токенов
    def validate(self, attrs):
        data = super().validate(attrs)

        # Добравляем нужное для возвращения вместе с acceess и refresh токенами
        data['id'] = self.user.id

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

