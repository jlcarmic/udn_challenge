from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^participants/new$',
        views.new_participant, name='new_participant'),
    url(r'^participants/update$',
        views.update_participant, name='update_participant'),
]
