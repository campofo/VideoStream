from django.db import models

# Create your models here.
class Videos(models.Model):
    title=models.TextField()
    description=models.TextField()
    video_file = models.FileField(upload_to='video')
    def __str__(self):
        return self.title