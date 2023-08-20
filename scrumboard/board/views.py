from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Task, User
from .serializers import RegistrationSerializer, TaskSerializer


class RegistrationViewSet(generics.ListCreateAPIView):
    print("Запустился RegistrationViewSet")
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    print("Завершился RegistrationViewSet")




class TaskAPIList(generics.ListCreateAPIView):
    print("Запустился TaskAPIList")
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print("Завершился TaskAPIList")

class TaskAPIUpdate(generics.UpdateAPIView):
    print("Запустился TaskAPIUpdate")
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print("Завершился TaskAPIUpdate")

class TaskAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    print("Запустился TaskAPIDestroy")
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print("Завершился TaskAPIDestroy")

def index(request):
    return render(request, "index.html")
