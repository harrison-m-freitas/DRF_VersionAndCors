# Generated by Django 4.2.7 on 2023-12-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_course_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
