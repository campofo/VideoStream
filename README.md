# Django Video Streaming App

A simple web application built with Django for uploading, viewing, and sharing videos. The app also includes user authentication and email verification.

## Features

- User authentication (signup, login, logout)
- Video upload and playback
- Video navigation (next/previous)
- Sharing video links
- Email verification for new users
- Admin interface for managing videos and users

## Requirements

- Python 3.8+
- Django 3.2+
- A working SMTP configuration for email verification

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/videostream.git
cd videostream
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
Create a .env file in the root directory with the following content:
```bash
SECRET_KEY=your_secret_key
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
```
### 5. Apply migrations
```bash
python manage.py migrate
```
### 6. Create a superuser
```bash
python manage.py createsuperuser
```
### 7. Collect static files
```bash
python manage.py collectstatic
```
### 8. Run the development server
```bash
python manage.py runserver
```
### 9. Access the application
Open your web browser and go to http://127.0.0.1:8000.


### Additional Notes

- Ensure to replace `yourusername`, `your_email@gmail.com`, and other placeholders with actual values.
- Modify the instructions based on your project's specifics, such as different dependencies or additional setup steps.
- If your project uses any third-party libraries or tools, be sure to mention them and include relevant setup instructions.

 ### Access the Deployed Application
You can access the deployed application at http://hunterperry08.pythonanywhere.com/.
Admin page(http://hunterperry08.pythonanywhere.com/admin)
```log
username:admin_boss
password:bigman
```
