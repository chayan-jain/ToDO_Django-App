from django.db import models
from django.urls import reverse
from django import forms

class Event(models.Model):

    Event_Name=models.CharField(max_length=256)
    Event_Date=models.DateField()
    Event_Time=models.TimeField()
    Event_Description=models.CharField(max_length=256)

    def __str__(self):
        return self.Event_Name

    def get_absolute_url(self):
        return reverse("app1:detail",kwargs={'pk':self.pk})
