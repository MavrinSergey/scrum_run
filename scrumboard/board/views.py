from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Task, User
from .serializers import RegistrationSerializer, TaskSerializer

"""представления создаются средствами DRF
    задача представлений обработка запроса и отправка данных пользователю
    задача по формированию запроса передается Сериализаторам"""


class RegistrationViewSet(generics.ListCreateAPIView):
    """Класс для обработки запросов к модели User"""

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Класс для обработки запросов к модели Task"""

    queryset = Task.objects.all().select_related('user')
    serializer_class = TaskSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return TaskSerializer

        return self.serializer_class


def index(request):
    return render(request, 'index.html')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  # Создаем пользовательский ответ на запрос токенов
    def validate(self, attrs):
        data = super().validate(attrs)

        # Добавляем нужное для возвращения вместе с access и refresh токенами
        data['id'] = self.user.id

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
