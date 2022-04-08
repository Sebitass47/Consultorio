# CONSULTORIO

## Demo
[Video](https://youtu.be/9JeWVEp5E6g)

## What is it?
It is an application designed for a medical clinic, in which patients can read health posts published by doctors, learn more about the clinic (where it is, mission, vision, history), schedule appointments, check their appointment time, or cancel your appointment.
Doctors can publish articles or posts on health issues, format it, adding images, links, fonts ...
Also making use of the / admin page that django provides you can review and modify the history of their patients, review the appointments they have and modify work hours.


## Why?
The idea for this project came about because I have a friend who is studying nutrition, and when I finished her degree she wants to set up her own practice, and every good practice has to have its own web application.

# Distinctiveness and complexity:

Among the technologies it uses are: Django (Python), SQL, Javascript, HTML, CSS and Bootstrap.
It is a complete web application, with a responsive design, and capable of storing patients, appointment times, posts and promotions. Larger than previous projects.
All the code is organized so that it is easy to edit.

### What’s contained in each file you created

**BlogCitas** contains the main code of our web application.
In the views.py file are all the paths that the user can access, such as: "main, blog, post, about_from, citations, new_date and delete_date".

In the file **api.py** you will find all the routes that are used for the Front end to obtain information, such as "registration and schedules".

In **functions.py** there are 2 functions that could have been included in api.py and views.py, but for organizational reasons I decided to put them in a different file.

In **models.py** you will find the necessary models to create the database, which in this case is sqlite, but it could easily be replaced by MySQL.

In the ** templates** folder there are all the html files that are used, and in the ** static ** folder there are the css file and the 3 javascript files.

**media** contains all the photos that are used in the interface, sqlite is used to organize them and every time you post new articles, they are saved in the folder.

**Consultorio** is the folder that Django creates when starting the project, modifies the file "settings.py" and "urls.py"

### What additional modules are used for the project?
tinymce
pillow

### How to run your application

You must open a terminal, and go to the path where you downloaded the project, execute the command `pip install -r requirements.py`. After installing the modules set in requirements.txt, you must perform the database migrations, with the commands: `python manage.py makemigrations`, and then `python manage.py migrate`. After that, just run `pyhton manage.py runserver` to access the app.

