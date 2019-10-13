from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Prescription(models.Model):
    image = models.ImageField(upload_to='images', default='default_image.jpg')
    result_image = models.ImageField(upload_to='result_image', default='default_image.jpg')
    medical_problem = models.CharField(max_length=200)
    doctor = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete =models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} with {self.medical_problem}'

    def get_absolute_url(self):
        return reverse('prescription_detail',kwargs={'pk':self.pk})

    


    
    
    
