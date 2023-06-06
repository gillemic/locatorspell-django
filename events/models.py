from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=100)
  tournament_organizer = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  event_type = models.CharField(max_length=100)
  category = models.CharField(max_length=10, blank=True, default='None')
  start_date = models.DateField("Start Date")
  end_date = models.DateField("End Date", blank=True, null=True)
  charity = models.BooleanField(blank=True, default=False)
  promoted = models.BooleanField(blank=True, default=False)
  price = models.PositiveIntegerField(default=0)
  url = models.CharField(max_length=100, blank=True, default='')
  description = models.CharField(max_length=1000)
  
  def __str__(self):
    return self.name
  
class KnownOrganizer(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=20, blank=True, null=True)
  email = models.EmailField(max_length=50, blank=True, null=True)
  contact_info = models.CharField(max_length=50, blank=True, null=True)
  website = models.CharField(max_length=50, blank=True, default='')
  location = models.CharField(max_length=100)
  notes = models.CharField(max_length=1000, blank=True, default='')
  calendar_link = models.CharField(max_length=50, blank=True, default='')
  
  def __str__(self):
    return self.name