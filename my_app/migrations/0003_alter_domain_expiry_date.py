# Generated by Django 4.2.3 on 2023-07-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
