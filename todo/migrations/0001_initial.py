# Generated by Django 2.1.2 on 2018-10-30 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('duedate', models.DateTimeField(verbose_name='마감기한')),
                ('done', models.BooleanField(verbose_name='완료')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]