from django.conf.urls import url
from . import views

# TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
