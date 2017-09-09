from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Video(models.Model):
    title= models.CharField(max_length=200)
    url_title= models.CharField(max_length=200)
    GENDER_CHOICES = (
    (0, 'Straight'),
    (1, 'Lesbian'),
    (2, 'Gay'),
    (3, 'Threesome (FMF)'),
    (4, 'Threesome (MMF)'),)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    MOOD_CHOICES= (
    (0, 'Soft'),
    (1, 'Intense'),
    (2, 'Rough'),)
    mood = models.IntegerField(choices=MOOD_CHOICES)
    TOPIC_CHOICES=(
    (0, 'Normal Romantic Stuff'),
    (1, 'BDSM'),
    (2, 'Toys and Machines'),
    (3, 'Blowjob'),
    (4, 'Anal'),
    (5, 'Female Masturbation'),
    (6, 'Other'),
    )
    topic = models.IntegerField(choices=TOPIC_CHOICES)
    RACE_CHOICES=(
    (0, 'Interacial'),
    (1, 'White'),
    (2, 'Black'),
    (3, 'Asian'),
    (4, 'Latino'),
    (5, 'Other'),
    )
    race = models.IntegerField(choices=RACE_CHOICES)
    photo = models.FileField(upload_to='photos/', blank=True, null= True)
    def __str__(self):
        return str(self.title)
