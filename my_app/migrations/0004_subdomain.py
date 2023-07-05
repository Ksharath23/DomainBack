# Generated by Django 4.2.3 on 2023-07-04 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_domain_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.domain')),
            ],
        ),
    ]
