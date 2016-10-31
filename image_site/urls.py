from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from image.views import UserCreateView, ImageListView, ImageCreateView, ImageUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', ImageListView.as_view(), name='image_list_view'),
    url(r'^image/upload/$', ImageCreateView.as_view(), name='image_create_view'),
    url(r'^image/update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
