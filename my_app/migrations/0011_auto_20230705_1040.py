# Generated by Django 3.2.12 on 2023-07-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20230705_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='certificate_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='certificate_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='domain_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
