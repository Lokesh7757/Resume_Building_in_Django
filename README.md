# Resume_Building_in_Django

Step-1) Start the Django Project
Create a new Django project and navigate into it:
django-admin startproject resume_builder
cd resume_builder

Step-2) Create the App
Create a new app within your project:
python manage.py startapp home

Step-3) Register the App
Add your app to the INSTALLED_APPS list in resume_builder/settings.py:

Step-4) Define URL Routes
In resume_builder/urls.py, include the URLs from your app:

Step-5)Create a urls.py file in the home app directory:

Step-6)Create Views
In home/views.py, define the views for the home page and resume generation:

Step-7)Create Templates
In home/templates/, create two HTML files: index.html and resume.html.

Step-8)Run the Server
Migrate the database and run the development server:
