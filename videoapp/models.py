from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.
class Videos(models.Model):
    title=models.TextField()
    description=models.TextField()
    video_file = models.FileField(upload_to='video')
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Videos)
def delete_video_file(sender, instance, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)