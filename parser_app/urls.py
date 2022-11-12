from django.urls import re_path as url
from parser_app import views

urlpatterns = [
    url(r'groups/(\d+)$', views.get_groups)   # вот тут задаётся урл к ресту
]