from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Internship(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('intern_detail', kwargs={'pk':self.pk})


class Entreprise(models.Model):
    name = models.CharField(max_length = 100)
    fullName = models.CharField(max_length = 100)
    description  = models.TextField()
    image = models.ImageField(default='images/defaultEntreprise.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.name
