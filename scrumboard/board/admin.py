from django.contrib import admin
from .models import User, Task, SignIn, StatusTask, Company, Project, StatusUserProjects, ProjectParticipants

admin.site.register(User)
admin.site.register(Task)
admin.site.register(SignIn)
admin.site.register(StatusTask)
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(StatusUserProjects)
admin.site.register(ProjectParticipants)