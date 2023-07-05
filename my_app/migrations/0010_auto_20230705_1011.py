# Generated by Django 3.2.12 on 2023-07-05 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20230705_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subdomain',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]