# Generated by Django 4.0.5 on 2022-06-26 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_verify_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verify_token',
            field=models.CharField(default=uuid.UUID('a9a540cd-ec99-4262-9ff3-19bbb54c3f38'), max_length=255, null=True),
        ),
    ]