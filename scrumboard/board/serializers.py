from rest_framework import serializers
from .models import User, Task, StatusTask, Project, Company, StatusUserProjects, ProjectParticipants


class RegistrationSerializer(serializers.ModelSerializer):
    print("Запустился RegistrationSerializer")
    class Meta:
        model = User
        fields = '__all__'

    print("Завершился RegistrationSerializer")

class ProjectSerializer(serializers.ModelSerializer):
    print("Запустился ProjectSerializer")
    class Meta:
        model = Project
        fields = '__all__'
    print("Завершился ProjectSerializer")


class CompanySerializer(serializers.ModelSerializer):
    print("Запустился CompanySerializer")
    class Meta:
        model = Company
        fields = '__all__'
    print("Завершился CompanySerializer")


class StatusUserProjectsSerializer(serializers.ModelSerializer):
    print("Запустился StatusUserProjectsSerializer")
    class Meta:
        model = StatusUserProjects
        fields = '__all__'
    print("Завершился StatusUserProjectsSerializer")


class ProjectParticipantsSerializer(serializers.ModelSerializer):
    print("Запустился ProjectParticipantsSerializer")
    class Meta:
        model = ProjectParticipants
        fields = '__all__'

    print("Завершился ProjectParticipantsSerializer")


class TaskSerializer(serializers.ModelSerializer):
    print("Запустился TaskSerializer")
    status = serializers.CharField(source='status.name')

    class Meta:
        model = Task
        fields = '__all__'

    print("Завершился TaskSerializer")

    def create(self, validated_data):
        return Task(**validated_data)


class StatusTaskSerializer(serializers.ModelSerializer):
    print("Запустился StatusTaskSerializer")
    class Meta:
        model = StatusTask
        fields = '__all__'

    print("Завершился StatusTaskSerializer")
