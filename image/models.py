from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.FileField()
    user = models.ForeignKey('auth.User')
    created_time = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        return self.picture.url
