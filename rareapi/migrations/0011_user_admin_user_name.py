# Generated by Django 4.2.7 on 2023-12-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0010_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
