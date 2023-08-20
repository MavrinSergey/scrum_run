from django.contrib import admin
from .models import User, Task, SignIn, StatusTask, Company, Project, StatusUserProjects, ProjectParticipants
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(Task)
admin.site.register(SignIn)
admin.site.register(StatusTask)
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(StatusUserProjects)
admin.site.register(ProjectParticipants)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    print("Запустился UserAdmin")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    print("Завершился UserAdmin")
