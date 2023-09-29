# Generated by Django 4.2.3 on 2023-08-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_user_managers_remove_signin_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectparticipants',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectparticipants',
            name='status_user_project',
        ),
        migrations.RemoveField(
            model_name='projectparticipants',
            name='user',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='to-work', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectParticipants',
        ),
        migrations.DeleteModel(
            name='SignIn',
        ),
        migrations.DeleteModel(
            name='StatusTask',
        ),
        migrations.DeleteModel(
            name='StatusUserProjects',
        ),
    ]