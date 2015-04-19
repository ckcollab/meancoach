import sys

from fabric.api import local, hide, settings
from fabric.contrib import django

sys.path.insert(0, ".")

django.settings_module('settings.local')
from django.conf import settings as django_settings


def test_django():
    local('py.test apps/**/tests/*.py')


def test_flake8():
    local('flake8 *.py')


def test_selenium():
    local('py.test tests/functional/*.py')


def test():
    test_flake8()
    test_django()
    test_selenium()


def fresh_db():
    print "%" * 80
    print " Starting from scratch!"
    print "%" * 80
    print ""

    # on heroku run heroku pg:reset DATABASEURL -- where database url is the
    # env variable, thats it!

    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        with settings(warn_only=True):
            sys.stdout.write("Dropping database...")
            local('dropdb %s' % django_settings.DATABASES['default']['NAME'])
            print "done"

            sys.stdout.write("Creating database...")
            local('createdb %s' % django_settings.DATABASES['default']['NAME'])
            print "done"

            sys.stdout.write("Syncdb and migrate...")
            local('python manage.py syncdb --noinput')
            print "done"

    sys.stdout.write("[TODO] *** Initialize repo with data...")
    # local('python manage.py init')
    # print "done"
