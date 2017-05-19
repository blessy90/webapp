# webapp
A Django project for simple webapp using python3 to return "Hello World." with some unit test cases.
The project accepts an Http request at /v1/sort which sorts and returns a set of integers.It also updates the number of times the http request is hit into the database.

To start with:
Need to install python and django(https://www.djangoproject.com/).

To run the project:
Go to the directory of the project in command line, run the following command

$ python manage.py runserver
Go to http://localhost:8000/webapp/ in your browser, and you should see the text "Hello World."

To run the test cases:
Go to the directory of the project in command line, run the following command

$ python manage.py test

To make the database up,run the following command

$python manage.py makemigrations
$python manage.py migrate

To visit the sort page,run the server using the above command,
then vist http://localhost:8000/webapp/v1/sort
check the command line to get the print messages.



