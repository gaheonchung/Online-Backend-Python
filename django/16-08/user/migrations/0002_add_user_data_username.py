# Generated by Django 5.0.2 on 2024-03-06 10:19

from django.db import migrations
from django.contrib.auth.models import User
from user.models import UserProfile

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    def add_user_data(apps, schema_editor):
        # 사용자 추가
        user = User.objects.create_user('username', 'username@example.com', 'password123!')
        # 사용자 프로필 추가
        UserProfile.objects.create(user=user, bio='안녕하세요!')

    def remove_user_data(apps, schema_editor):
        try:
            # 사용자 프로필 삭제
            UserProfile.objects.get(user__username='username').delete()
        except UserProfile.DoesNotExist:
            pass

        try:
            # 사용자 삭제
            User.objects.get(username='username').delete()
        except User.DoesNotExist:
            pass

    operations = [
        migrations.RunPython(add_user_data, remove_user_data),
    ]
