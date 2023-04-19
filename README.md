#For Kivy - Cross Platform Application 

Must follow 
https://kivy.org/doc/stable/gettingstarted/installation.html

This provide Installation to OpenGl and kivy Library, with events and its work flow

Python plays major role here to create application

# For Google MLKit API
Speech recognizer - SFSpeechRecognizer - Native module
	
	- For recognising user speech. Default language is “en-US”. For more info refer SpeechRecognizer.swift in Helpers folder. For documentation refer https://developer.apple.com/documentation/speech/sfspeechrecognizer.



# This FOR Python APIs and database connection

This is lANGUAGE_Tech app that allows users to translate text from one language to another.

# Requirements

Before running the app, make sure you have the following dependencies installed:

    Python 3.8 or higher
    Django 3.2 or higher
    translate (a Python library for language translation)

You can install the required Python packages by running the following command:

    pip install -r requirements.txt

# Database Migrations

Before running the app, you will need to apply the database migrations. To do this, run the following command:

    python manage.py migrate

#Starting the Server
To start the development server, run the following command:

    python manage.py runserver

The server will now be running at http://localhost:8000/.

# Endpoints

The app has the following endpoints:

    /admin: The Django admin site, where you can manage the app's models and data.
    /translate: The endpoint for translating text from one language to another.

# Accessing the Admin Site

To access the admin site, you will need to create a superuser. To do this, run the following command:

    python manage.py createsuperuser
    # after executing you can ask for username/password add and last give 'y' so with that credentials you can acces admin site.

Follow the prompts to enter a username, email, and password for the superuser.
Once the superuser is created, you can access the admin site at http://localhost:8000/admin/.

Accessing the Translate Endpoint
To access the /translate endpoint, simply navigate to http://localhost:8000/translate in your web browser. You can then enter the text you want to translate and select the source and target languages.

# Test Cases Check for the Project

Execute the command as following:

    python manage.py test
