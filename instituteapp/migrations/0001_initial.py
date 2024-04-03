# Generated by Django 4.2.7 on 2023-12-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_fee', models.IntegerField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('course_start_date', models.DateField(max_length=50)),
                ('course_end_date', models.DateField(max_length=50)),
                ('course_duration', models.CharField(max_length=50)),
                ('course_timings', models.TimeField(max_length=50)),
                ('trainer_name', models.CharField(max_length=50)),
            ],
        ),
    ]