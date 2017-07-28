

# rblmonitor

rblmonitor is an app to check if an IP is blacklisted.
It is built with [Python][0] using the [Django Web Framework][1].
And bootstraped with [Django Edge][2]

This project has the following basic apps:

* rbls (just put the ip and check the status in the rbl sites)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv rblmonitor`
    2. `$ . rblmonitor/bin/activate`

Install all dependencies:
    pip3 install -r requirements.txt

Copy local.sample.env to local.env.
!!Important!! Generate a new SECRECT_KEY

Run migrations:
    python3 manage.py migrate
    
Import the data from the fixture:
    python3 manage.py loaddata rbllist

Create super user:
    python3 manage.py createsuperuser

Run the application:
    python3 manage.py runserver

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://django-edge.readthedocs.io/en/latest/
