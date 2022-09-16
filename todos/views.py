from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    """
    Lists all items in the Todo table, based on all the entries in the Todo table and uses the serializers.py 
    file to properly serialize the information
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    """
    Lists a specific entry in the Todo table listing everything in that one entry
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


