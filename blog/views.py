from django.shortcuts import render

# Create your views here.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
