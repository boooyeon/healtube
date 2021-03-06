# Generated by Django 2.2.7 on 2019-12-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.TextField()),
                ('health_type', models.TextField()),
                ('health_part', models.TextField()),
                ('video_title', models.CharField(max_length=100)),
                ('video_link', models.TextField()),
                ('video_view_num', models.TextField()),
                ('video_upload_date', models.TextField()),
            ],
        ),
    ]
