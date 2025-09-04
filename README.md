# Login & Signup System

A simple **Login and Signup system** built with Python (Django framework) and a basic frontend.  
This project demonstrates user authentication, registration, and session handling.

## Features
- User registration (signup)  
- User login & logout  
- Password hashing for security
- Frontend validation with simple error messages 

## ⚙️ Setup Instructions

### Clone this repo
git clone https://github.com/vamshikrishna-piska/login-signup.git
cd login-signup

python -m venv venv
venv\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt
python manage.py migrate

## Now start the server 
python manage.py runserver

Once the server is running, open **http://127.0.0.1:8000/api/auth/page/** in your browser
That’s where you can access the Login/Signup page.
