from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    "A blog that user can record some diary."
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        "show title and some text"
        return self.title.title()