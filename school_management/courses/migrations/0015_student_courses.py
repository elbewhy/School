# Generated by Django 4.1.5 on 2023-06-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(through='courses.Registration', to='courses.course'),
        ),
    ]