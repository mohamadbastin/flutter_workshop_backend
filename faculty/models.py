from django.db import models


# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=11024)
    subject_groups = models.CharField(max_length=10241)
    research_interests = models.CharField(max_length=11024)
    email = models.CharField(max_length=256)
    pic = models.CharField(max_length=256)

    def __str__(self):
        return self.name
