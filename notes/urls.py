from django.urls import path

from . import views

#https://docs.djangoproject.com/en/3.2/topics/http/urls/
urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('taglist',views.taglist, name='taglist'),
    path('taglist/<str:tag_str>', views.tags ,name='tags')
]