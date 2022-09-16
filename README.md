## django-todo-api
A simple todo-api built using Django and DjangoRestFramework

First install required packages using `pip`:
    `pip install requirements.txt`
    
Then create a db using migrate
    `python manage.py migrate`
    
Create a superuser
    `python manage.py createsuperuser`
    
Make migrations to update the database
    `python manage.py makemigrations todo`
    
Migrate to update the database tables
    `python manage.py migrate`
    
At this point, you should have a basic Todo api, ready to be connected with a front-end, to start the server
    `python manage.py runserver`
    
This Todo app does not support multiuser lists, so every user create can add to the main todo list, The todo list does have to be updated from the admin page
  logging into with the superuser account created.
