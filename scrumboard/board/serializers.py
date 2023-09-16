from rest_framework import serializers
from .models import User, Task, StatusTask, Project, Company, StatusUserProjects, ProjectParticipants


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class StatusUserProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusUserProjects
        fields = '__all__'


class ProjectParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectParticipants
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status.name')

    class Meta:
        model = Task
        fields = '__all__'


class StatusTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusTask
        fields = '__all__'
