# todos/urls.py
from django.urls import path

from .views import ListTodo, DetailTodo


urlpatterns = [
        # gives a url to each individual item in the Todo table
        path("<int:pk>/", DetailTodo.as_view(), name="todo_detail" ),
        # path to view all items in Todo table
        path("", ListTodo.as_view(), name="todo_list"),
        ]
