from django.db import models
from datetime import datetime

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=225, default='The Book')
    author = models.CharField(max_length=225, default='anonymous')
    details = models.TextField(max_length=500)
    created_at = models.DateField(default=datetime.now)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"
