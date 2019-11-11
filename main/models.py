from django.db import models

# Create your models here.
class Channel(models.Model):
    channel_name = models.TextField()
    health_type = models.TextField()
    health_part = models.TextField()
    video_title= models.CharField(max_length=100)
    video_link = models.TextField()
    video_view_num = models.TextField()
    video_upload_date = models.TextField()

    def __str__(self):
        return self.video_title
