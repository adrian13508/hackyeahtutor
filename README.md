## Basics

1. Create and activate virtual env for the project
   1. python -m venv env
   2. source env/bin/activate
2. Start django dev server with python manage.py runserver
3. Start tailwind server for CSS styling in development with python manage.py tailwind start


## Production 

Besides deploying django app, static files from tailwind must be generated.
1. python manage.py tailwind build
2. python manage.py collectstatic

