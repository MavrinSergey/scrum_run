from rest_framework import generics, viewsets

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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print("Завершился TaskViewSet")
