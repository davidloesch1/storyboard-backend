import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Plot(models.Model):
    FIRST = 'First'
    SECOND = 'Second'
    THIRD = 'Third'
    NA = 'N/A'
    POV_Choices = (
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Third'),
        (NA, 'N/A')
    )
    title = models.CharField(max_length=150)
    blurb = models.CharField(max_length=150)
    pov = models.CharField(max_length=6, choices=POV_Choices, default=NA)
    setting = models.TextField()
    theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    plot = models.TextField(blank=False)
    user = models.ForeignKey(User, models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Character(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)
    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name


class Submission(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150)
    blurb = models.CharField(max_length=150)
    selected = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    addition = models.TextField(blank=False)
    chapter = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title
