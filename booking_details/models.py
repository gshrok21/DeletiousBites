from django.db import models

# Create your models here.
class bookings(models.Model):
    name=models.CharField(max_length=30)
    guests=models.IntegerField()
    date=models.DateField(auto_now=False,auto_now_add=False)
    time=models.TimeField(auto_now=False,auto_now_add=False)
    requests=models.TextField()
    code=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    
class view_review(models.Model):
    reviewer=models.CharField(max_length=30)
    review=models.TextField()
class upload_file(models.Model):
    file=models.FileField(upload_to='image/')