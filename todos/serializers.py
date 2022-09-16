# todos/serializers.py

from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer class for items based on the Todo model, using the default id field Django autogenerates
    """
    class Meta:
        model = Todo
        fields = (
                "id",
                "title",
                "body",
                )
