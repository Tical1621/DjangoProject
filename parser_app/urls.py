from django.urls import path
from parser_app import views

urlpatterns = [
    path('groups/<int:group_id>', views.get_groups)   # вот тут задаётся урл к ресту
]