from django.contrib import admin
from image.models import Image, Comment, Category

admin.site.register([Image, Comment, Category])
