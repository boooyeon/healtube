from django.db import models

# Create your models here.
class Channel(models.Model):
    objects = models.Manager()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    channel_name = models.TextField()
    health_type = models.TextField()
    health_part = models.TextField()
    video_title= models.CharField(max_length=100)
    video_link = models.TextField()
    video_view_num = models.TextField()
    video_upload_date = models.TextField()


        
    # def __str__(self):
    #      return self.video_title

# class MySearch(models.Model):
#     objects = models.Manager()
#     channel_name = models.ForeignKey(Channel, db_column='channel_name', on_delete=models.CASCADE)
#     health_type = models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)
#     health_part = models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)
#     video_title= models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)
#     video_link = models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)
#     video_view_num = models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)
#     video_upload_date = models.ForeignKey(Channel, db_column='channel_name',on_delete=models.CASCADE)

        
#     def __str__(self):
#         return self.video_title
