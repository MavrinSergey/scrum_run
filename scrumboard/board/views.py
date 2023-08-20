from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import RegistrationSerializer, TaskSerializer, ProjectSerializer, CompanySerializer, \
    StatusUserProjectsSerializer, ProjectParticipantsSerializer
from .models import Task, User, Project, Company, StatusUserProjects, ProjectParticipants


class RegistrationViewSet(generics.ListCreateAPIView):
    print("Запустился RegistrationViewSet")
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    print("Завершился RegistrationViewSet")


class ProjectViewSet(viewsets.ModelViewSet):
    print("Запустился ProjectViewSet")
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    print("Завершился ProjectViewSet")


class CompanyViewSet(viewsets.ModelViewSet):
    print("Запустился CompanyViewSet")
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    print("Завершился CompanyViewSet")


class StatusUserProjectsViewSet(viewsets.ModelViewSet):
    print("Запустился StatusUserProjectsViewSet")
    queryset = StatusUserProjects.objects.all()
    serializer_class = StatusUserProjectsSerializer
    print("Завершился StatusUserProjectsViewSet")


class ProjectParticipantsViewSet(viewsets.ModelViewSet):
    print("Запустился ProjectParticipantsViewSet")
    queryset = ProjectParticipants.objects.all()
    serializer_class = ProjectParticipantsSerializer
    print("Завершился ProjectParticipantsViewSet")

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
