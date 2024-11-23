from .models import Movie
from rest_framework import serializers

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id','name','genre','rating']
        