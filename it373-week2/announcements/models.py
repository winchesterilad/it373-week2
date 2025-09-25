from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
