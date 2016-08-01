# djangoREST

Django REST framework is a powerful and flexible toolkit for building Web APIs.


To use, clone the repo.
copy (git clone https://github.com/skafis/djangoREST.git)

create a Virtual enviroment - virtualenv venv
activate the virtual enviroment - source venv/bin/activate

install the required packages to run  - pip install -r requirements.txt

Prepare the Database - python manage.py makemigrations
Create the Database - python manage.py migrate

create admin- python manage.py createsuperuser

run the server - python manage.py runserver

install httpie package - sudo apt-get install httpie

run http -a username:password http://127.0.0.1:8000/users/
replace username and password with the one you created on python manage.py createsuperuser
