<h1 align="center">HEXYZ Project</h1>

<p align="center">
	<img src="static/images/logo.png" alt="HEXYZ Project logo">
</p>

<p align="center">Simple bank of virtual money - HEXYZ (HXZ).</p>

## Info
- This is a fun project.
- This is not a real bank or a cryptobank.
- This is not a cryptocurrency too.

## Requirements

```
PC or a mobile device with Termux
The simplest CPU (1 GHz at least)
About 256 MB of free RAM
About 1 GB free space on disk
Hand(s), palm(s) and finger(s)
Brain and common sense
Eye(s)
```

```
Windows >= 7
OR
Ubuntu >= 18.04
OR
Linux Mint >= 18
OR
Other linux >= ¯\_(ツ)_/¯ (IDK versions, check for yourself)
OR
Android >= 6 (I recommend to use at least 7th version)
```

```
Python >= 3.7
Git (no matter what version, but preferably the latest (2.27 at the moment))
Pip (no matter what version, but preferably the latest (20.1.1 at the moment))
Django >= 3.0.7
Django-allauth >= 0.42.0
Django-profiles >= 0.2
All actual dependencies of the above libraries and programs.
```

## How to run the website
```bash
cd ~
git clone https://github.com/hilight3r/HEXYZ.git
cd HEXYZ
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
#here you will need to type your login, email and password to get access to control panel
python manage.py runserver
```
  *If this commands don't work, try replace `python` to `python3` and/or `pip` to `pip3`*
- You will find your website on `http://127.0.0.1:8000` by default. You can change IP and port of your server, added `ip:port` after `runsever` argument of the last command.
- Control panel will be on `http://127.0.0.1:8000/admin`.
