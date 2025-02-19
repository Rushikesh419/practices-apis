from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    rating=models.FloatField()
    
    def __str__(self):
        return f"{self.name} ({self.genre}) - Rating: {self.rating}"