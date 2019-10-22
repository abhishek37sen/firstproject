from django.db import models
from multiselectfield import MultiSelectField
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_duration=models.CharField(max_length=100)
    course_start_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.CharField(max_length=100)

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=200)
    date=models.DateTimeField(max_length=50)

class Enquiry_Data(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=10)
    CORSESS_CHOISES=(
        ('PY',"PYTHON"),
        ('DJ','Django'),
        ('RA','Rest  Api')
    )
    course=MultiSelectField(choices=CORSESS_CHOISES)
    SHIFTS_CHOISES=(
        ('Morning','Morning shift'),
        ('Afternoon','Afternoon_shift'),
        ('Evening','Evening_shift'),
        ('Night','Night_shift')
    )
    shifts=MultiSelectField(choices=SHIFTS_CHOISES)
    start_date=models.DateTimeField(max_length=100)
