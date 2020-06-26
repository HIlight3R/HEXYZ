# HEXYZ
_Simple bank of virtual money - HEXYZ (HXZ)._

## Info
- This is a fun project.
- This is not a real bank or a cryptobank.
- This is not a cryptocurrency too.

## How to run the website
- Clone the repository or download archive with it.
- Check your Python version, it should be at least `3.7`.
- Go to the root of the project directory.
- Run the following commands in your terminal (in root directory):
  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  (here you will need to enter your login, email and password to get access to control panel)
  python manage.py runserver
  ```
- You will find your website on http://127.0.0.1:8000 by default. You can change IP and port of your server, added `ip:port` after `... runsever`
- Control panel will be on http://127.0.0.1:8000/admin.
