from django.db import models

# Create your models here.


class post(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name
