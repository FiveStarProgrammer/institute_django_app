from django.db import models

# Create your models here.
class CourseData(models.Model):
    course_name=models.CharField(max_length=50)
    course_fee=models.IntegerField(max_length=50)
    institute_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    course_start_date=models.DateField(max_length=50)
    course_end_date=models.DateField(max_length=50)
    course_duration=models.CharField(max_length=50)
    course_timings=models.TimeField(max_length=50)
    trainer_name=models.CharField(max_length=50)


class FeedBackData(models.Model):
    feedback = models.TextField(max_length=500)
