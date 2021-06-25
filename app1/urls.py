from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name='app1'
urlpatterns= [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^register/$', views.register,name="register"),
    # url(r'^register/$',views.UserFormView.as_view(), name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app1/login.html'),name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='app1/logout.html'),name="logout"),
    url(r'album/(?P<pk>[0-9]+)/addphoto/$', views.PhotoCreate.as_view(), name='photo-add'),
    url(r'album/(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),


]