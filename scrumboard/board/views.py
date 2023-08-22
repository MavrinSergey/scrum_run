from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer

        return self.serializer_class
