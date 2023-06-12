from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=50)
  date_posted = models.DateTimeField()
  post = models.CharField(max_length=1000)
  
  def __str__(self):
    return self.title