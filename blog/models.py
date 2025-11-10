from django.db import models
from django.utils import timezone




class Blog(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_thumbnails/')
    date_posted = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    
