# Generated by Django 5.0.4 on 2024-04-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_options_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.AddField(
            model_name='message',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]