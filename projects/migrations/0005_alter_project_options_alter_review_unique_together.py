# Generated by Django 5.0.4 on 2024-04-10 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options_review_user'),
        ('users', '0003_alter_profile_options_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-votes_ratio', '-votes_total']},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'project')},
        ),
    ]
