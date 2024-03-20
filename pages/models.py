from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

CHOICES = [
    ("content", "Content"),
    ("video", "Video"),
]


class Page(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=15, choices=CHOICES)

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tutorials')
    content = CKEditor5Field('Content', config_name='extends')

    def __str__(self):
        return self.content


class Video(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()

    def __str__(self):
        return self.video_url
