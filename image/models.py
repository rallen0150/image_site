from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.FileField()
    user = models.ForeignKey('auth.User')
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('image.Category')

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return self.picture.url

    @property
    def get_comment(self):
        return Comment.objects.filter(comment_image=self)

class Comment(models.Model):
    comment = models.TextField()
    comment_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')
    comment_image = models.ForeignKey(Image)

    def __str__(self):
        return self.comment

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    def get_recent(self):
        return Image.objects.filter(category=self).order_by('created_time')

    def __str__(self):
        return self.title
