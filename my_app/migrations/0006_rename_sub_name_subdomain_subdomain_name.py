# Generated by Django 4.2.3 on 2023-07-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_subdomain_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdomain',
            old_name='sub_name',
            new_name='Subdomain_name',
        ),
    ]