from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from image.views import IndexView, CategoryDetailView, CategoryListView, UserCreateView, ImageListView, \
                        CategoryCreateView, ImageCreateView, ImageUpdateView, ImageDetailView, CommentCreateView, \
                        CommentUpdateView, CategoryUpdateView, ImageDeleteView, CommentDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^category/$', CategoryListView.as_view(), name='category_list_view'),
    url(r'^category/create/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
    url(r'^category/(?P<pk>\d+)/update/$', CategoryUpdateView.as_view(), name='category_Update_view'),
    url(r'^image/$', ImageListView.as_view(), name='image_list_view'),
    url(r'^image/upload/$', ImageCreateView.as_view(), name='image_create_view'),
    url(r'^image/update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update_view'),
    url(r'^image/(?P<pk>\d+)/$', ImageDetailView.as_view(), name='image_detail_view'),
    url(r'^image/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^image/(?P<pk>\d+)/delete/$', ImageDeleteView.as_view(), name="image_delete_view"),
    url(r'^(?P<pk>\d+)/update_comment/$', CommentUpdateView.as_view(), name="comment_update_view"),
    url(r'^(?P<pk>\d+)/delete/$', CommentDeleteView.as_view(), name="comment_delete_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
