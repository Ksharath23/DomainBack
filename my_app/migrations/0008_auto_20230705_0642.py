# Generated by Django 3.2.12 on 2023-07-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_rename_host_domain_registrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
