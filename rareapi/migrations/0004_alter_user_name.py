# Generated by Django 4.1.3 on 2023-12-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_user_admin_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
