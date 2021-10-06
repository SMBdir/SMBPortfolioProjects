Requirements:
- Python 3.8.5
- Django 3.2.5 (can be pip installed using: pip3 install django)
- Mechanize 0.4.7 (can be pip installed using: pip3 install mechanize)
- SQLite3 3.34.1.0

Structure:
The web application's main functionality is stored in the lumi directory(LumiWebApp-main\luminescence_dating\lumi). 
Inside LumiWebApp-main\luminescence_dating\lumi, the most important files you will find are:
-call_to_drac.py 
-views.py
-urls.py
-models.py
-forms.py
-templates folder containing the .html templates
-tests folder containing unit tests

Also of interest LumiWebApp-main\luminescence_dating\manage.py

Run Django:
Once the requirements are installed on your machine open a command prompt and navigate to the project dir.
Once there navigate to: LumiWebApp-main\luminescence_dating\
From here run the command: Python3 manage.py runserver
This will then prompt you with the local address the web application is hosted at, usually: http://127.0.0.1:8000/
