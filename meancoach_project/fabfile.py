import sys

from fabric.api import local, hide, settings
from fabric.contrib import django

sys.path.insert(0, ".")

django.settings_module('settings.local')
from django.conf import settings as django_settings


def test_django():
    local('py.test apps/**/tests/*.py', capture=True)


def test_flake8():
    local('flake8 *.py', capture=True)


def test_selenium():
    local('py.test tests/functional/*.py', capture=True)


def test():
    print "%" * 80
    print " Running tests..."
    print "%" * 80
    print ""

    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        sys.stdout.write("Checking syntax...")
        test_flake8()
        print "done"

        sys.stdout.write("Running Django tests...")
        test_django()
        print "done"

        sys.stdout.write("Running Selenium tests...")
        test_selenium()
        print "done"


def fresh_db():
    print "%" * 80
    print " Starting from scratch!"
    print "%" * 80
    print ""

    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        with settings(warn_only=True):
            database_name = django_settings.DATABASES['default']['NAME']
            database_engine = django_settings.DATABASES['default']['ENGINE']

            if database_engine == 'django.db.backends.sqlite3':
                sys.stdout.write("Dropping database...")
                local('rm sqlite_database')
                print "done"
            elif database_engine == 'django.db.backends.postgresql_psycopg2':
                sys.stdout.write("Dropping database...")
                local('dropdb %s' % database_name)
                print "done"

                sys.stdout.write("Creating database...")
                local('createdb %s' % database_name)
                print "done"

            sys.stdout.write("Syncdb and migrate...")
            local('python manage.py syncdb --noinput')
            local('python manage.py migrate')
            print "done"

            sys.stdout.write("Making super user admin//admin...")
            local("echo \"from django.contrib.auth.models import User; "
                  "User.objects.create_superuser('admin', 'admin@example.com',"
                  " 'admin')\" | python manage.py shell")
            print "done"

    sys.stdout.write("[TODO] *** Initialize repo with data...")
    # local('python manage.py init')
    print "done"
