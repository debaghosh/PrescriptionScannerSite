from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    usertype = [
        ('Patient', 'Patient'),
        ('Doctor','Doctor')
    ]

    gender = [
        ('Male','Male'),
        ('Female','Female')
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_gender = models.CharField(max_length=6, default='Gender', choices=gender)
    user_type = models.CharField(max_length=7, default='Usertype', choices=usertype)


    
    
    def __str__(self):
        return f'{self.user.username} + {self.user_type} Profile'

"""
class user_type(models.Model):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
         if self.is_student == True:
             return self.user.username + " - is_student"
         else:
             return self.user.username + " - is_teacher"
"""