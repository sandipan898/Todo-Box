# Generated by Django 3.0.6 on 2020-05-10 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_list', '0002_auto_20200510_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
