from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    cuisineType = models.CharField(max_length=50)


    def __str__(self):
        return self.name