from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='crops_index'),
    url('add/$', views.create, name='crops_add'),
    url(r'(?P<crop_id>[0-9]+)/$', views.detail, name='crops_detail'),
    url(r'(?P<crop_id>[0-9]+)/edit$', views.update, name='crops_edit'),
]
