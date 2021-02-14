from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("task1:post_single", args=[self.slug])
    