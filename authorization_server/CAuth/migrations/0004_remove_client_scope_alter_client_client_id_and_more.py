# Generated by Django 4.0.5 on 2022-06-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAuth', '0003_alter_client_client_id_alter_client_client_secret_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='scope',
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(default='584c805e7b535757714aa382e3c5968e', max_length=1000),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_secret',
            field=models.CharField(default='329c530bed5146f657e0652847c2c58276ffed6a768deeb2cafc0c53823e7e86', max_length=1000),
        ),
    ]
