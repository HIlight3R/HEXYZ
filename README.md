# THE PROJECT IS CLOSED, NO FURTHER DEVELOPMENT IS PLANNED!

<p align="center">
	<img src="static/images/logo.png" alt="Логотип проекта HEXYZ">
</p>

<p align="center">A simple demonstration of Python Django v3 using a simple virtual bank as an example.</p>
<p align="center">This project was created during my learning of the framework, so don't judge it too harshly.</p>

## Info
- This is just a demo project.
- This is not a real banking system.
- It is dangerous to use if you want to use it for real money or cryptocurrencies.
- HEXYZ is not a cryptocurrency.

## System requirements

- Python (version 3.7 or newer)
- Git
- PIP
- `python-django` (version 3.*)
- `django-allauth` compatible with Django version
- `django-profiles` compatible with Django version
- `django-grappelli` compatible with Django version

## How to launch HEXYZ?
- In the `HEXYZ/settings.py` file, uncomment the line containing the `STATIC_ROOT` constant.
- Run in your shell:
  ```bash
  git clone https://github.com/HIlight3R/HEXYZ.git
  cd HEXYZ
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  # Here you will be asked to enter your login, password and email for the superuser account.
  python manage.py collectstatic
  python manage.py runserver
  ```
  *If the commands don't work, try using `python3` or `py -3` instead of `python` and `pip3` instead of `pip`*.
  *If you get errors when starting, comment out the line with the `STATIC_ROOT` constant in `HEXYZ/settings.py`*.
- By default, the site will be available at `http://127.0.0.1:8000`. You can change the IP address and port of the site by adding them in the format `ip:port` after the `runsever` argument of the last command. You can also make your site listen on all IPs available to you by using the format `0.0.0.0:port`.
- The site's admin panel will be located at `http://ip:port/admin` (by default `http://127.0.0.1:8000/admin`).
- When making changes to the `.py` project files, the site automatically reloads.
- To stop, enter the key combination `Ctrl+C` in the terminal where the HEXYZ is running.

## Setting up a site for production
The site does not require detailed configuration, everything is ready to work. But there are moments that are very important for the site's security.

***Attention!*** Before publishing the site to the public Internet, please make the following changes in the site settings file `HEXYZ/settings.py`:
- Change the value of `SECRET_KEY` to your own and do not publish it to the public. To do this, use [this](https://djecrety.ir) service to generate it.
- Change the value of `DEBUG` to `False`.
- In [square brackets], add in quotation marks ('single' or "double"), separated by commas, all web addresses that your site will process, assigning the list to the constant `ALLOWED_HOSTS`. For example, `ALLOWED_HOSTS = ['example.org', '.example.org', '*.example.org', 'subdomain.example.org', '123.45.67.89']`.
- In the cases of 'example.org'` and `'123.45.67.89'` everything is clear. The site will process the corresponding domain and IP address.
- In the case of `'.example.org'` (note the dot at the beginning), the site will process all subdomains of the domain __including__ the domain itself.
- In the case of `'*.example.org'`, the site will process all subdomains of the domain ***excluding*** the domain `mysite.ru` itself.
- In the fourth case (`'subdomain.example.org'`), the site will process ***only*** the subdomain, ***excluding*** the domain itself.
- It is not recommended to configure the `ALLOWED_HOSTS` parameter so that its elements overlap each other (for example, `ALLOWED_HOSTS = ['example.org', '.example.org']` (`'.example.org'` already includes `'example.org'`).
- For distributing static files in production, Django recommends using Nginx. For correct operation, use MacOS or Linux, on Windows, Nginx may cause undefined behavior.
- If for some reason you cannot or do not want to use Nginx, then use the `--insecure` flag at the end of the `python manage.py runserver ...` command. However, note that Django does not recommend doing this.

## License
The project is licensed under the free open source license MIT. You can read it in the `LICENSE` file in the root of the project. Please note that the license does not provide any guarantees at all and requires copyright to be indicated when copying the project.
