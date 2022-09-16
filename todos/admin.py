from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    """
    TodoAdmin allows the admin to make updates to the Todo model, as well as lists the title and 
    text in the body
    """
    list_display = (
            "title",
            "body",
            )

# adds the table to the admin site
admin.site.register(Todo, TodoAdmin)
