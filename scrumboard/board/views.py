from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import RegistrationSerializer, TaskSerializer, ProjectSerializer, CompanySerializer, \
    StatusUserProjectsSerializer, ProjectParticipantsSerializer
from .models import Task, User, Project, Company, StatusUserProjects, ProjectParticipants


class RegistrationViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class StatusUserProjectsViewSet(viewsets.ModelViewSet):
    queryset = StatusUserProjects.objects.all()
    serializer_class = StatusUserProjectsSerializer


class ProjectParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ProjectParticipants.objects.all()
    serializer_class = ProjectParticipantsSerializer


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    return render(request, "index.html")
