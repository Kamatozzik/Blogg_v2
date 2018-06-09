from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.sign_in, name='sign_in'),
    url(r'^post/(?P<pk>\d+)/$', views.post_info, name='post_info'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^posts/$', views.post_list, name='post_list'),

]
