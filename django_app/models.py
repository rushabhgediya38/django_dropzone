from django.db import models

# Create your models here.


class post(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name


class post_post(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post_post/', null=True, blank=True)

    def __str__(self):
        return self.name


class post123(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='post_post/img1/', null=True, blank=True)
    img = models.ImageField(upload_to='post_post/', null=True, blank=True)

    def __str__(self):
        return self.name
