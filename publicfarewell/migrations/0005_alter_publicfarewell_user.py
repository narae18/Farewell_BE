# Generated by Django 4.2.7 on 2023-11-08 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicfarewell', '0004_publicfarewell_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicfarewell',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
