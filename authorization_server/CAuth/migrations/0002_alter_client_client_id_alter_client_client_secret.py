# Generated by Django 4.0.5 on 2022-06-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(default='f5ad5b7b76d9bce481b53a5e71dfc648', max_length=1000),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_secret',
            field=models.CharField(default='49edd65700171ba96378d7ded988e73eeeda09fc25c8861d607b61672232e885', max_length=1000),
        ),
    ]
