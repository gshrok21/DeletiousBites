from django.db import models

# Create your models here.
class menu_des(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    about=models.CharField(max_length=60)
    ingredients=models.TextField()
    badge=models.CharField(max_length=30,blank=True)
    STATUS_CHOICES = [
    ('v', 'Vegetarian Dishes'),
    ('nv', 'Non-Vegetarian Dishes')]
    variant = models.CharField(max_length=25, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.title
