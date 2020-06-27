<h1 align="center">HEXYZ Project</h1>

<p align="center">
	<img src="./static/images/logo-small.png" alt="HEXYZ Project logo">
</p>

<p align="center">Simple bank of virtual money - HEXYZ (HXZ).</p>

## Info
- This is a fun project.
- This is not a real bank or a cryptobank.
- This is not a cryptocurrency too.

## How to run the website
- Clone the repository or download archive with it.
- Check your Python version, it should be at least `3.7`.
- Go to the root of the project directory.
- Run the following commands in your terminal (in the root directory):
  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  #(here you will need to type your login, email and password to get access to control panel)
  python manage.py runserver
  ```
- You will find your website on `http://127.0.0.1:8000` by default. You can change IP and port of your server, added `ip:port` after `runsever` argument of the last command.
- Control panel will be on `http://127.0.0.1:8000/admin`.
