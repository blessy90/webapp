from django.conf.urls import  url
from  . import views

"""To call the view"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^v1/sort/', views.post, name='sort')
]