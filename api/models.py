from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True, null=True)
    done = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:20]}...'