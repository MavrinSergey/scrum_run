from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .serializers import RegistrationSerializer, TaskSerializer, ProjectSerializer, CompanySerializer, \
    StatusUserProjectsSerializer, ProjectParticipantsSerializer
from .renderers import UserJSONRenderer
from .models import Task, SignIn, StatusTask, User, Project, Company, StatusUserProjects, ProjectParticipants


class RegistrationViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    #
    # serializer_class = RegistrationSerializer
    # renderer_classes = (UserJSONRenderer,)
    #
    # def post(self, request):
    #     user = request.data.get('user', {})
    #
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class TaskAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)


def index(request):
    return render(request, "index.html")
