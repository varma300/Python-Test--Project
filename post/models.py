from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
    def __str__(self):          # for display title nae in admin page
        return f"{self.title}" 