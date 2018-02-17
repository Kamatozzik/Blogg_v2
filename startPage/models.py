from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    creDate = models.TimeField(default=timezone.now)
    pubDate = models.TimeField(blank=True, null=True)

    def publish(self):
        self.pubDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title