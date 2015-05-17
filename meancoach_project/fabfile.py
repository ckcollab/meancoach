import sys

from fabric.api import local, hide, settings
from fabric.contrib import django

sys.path.insert(0, ".")

django.settings_module('settings.local')
from django.conf import settings as django_settings


def _print(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def _py_test(test_command, test_name):
    if test_name:
        test_name = '-k %s' % test_name
    local('%s %s' % (test_command, test_name), capture=True)


def test_e2e(k=''):
    '''Optionally pass 'k' argument to filter by test name, i.e.:
    fab test_e2e:k=test_pipeline_compiles_javascript_properly'''
    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        _print("Running Selenium tests...")
        _py_test('py.test tests/functional/*.py', k)
        print "done"


def test_django(k=''):
    '''Optionally pass 'k' argument to filter by test name, i.e.:
    fab test_e2e:k=test_pipeline_compiles_javascript_properly'''
    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        _print("Running Django tests...")
        _py_test('py.test apps/**/tests/*.py', k)
        print "done"


def test_lint():
    with hide('running', 'stdout', 'stderr', 'warnings', 'aborts'):
        _print("Checking syntax...")
        local('flake8 . --exclude=*/migrations/* --max-line-length=120 --ignore=F403',
              capture=True)
        print "done"


def test():
    print "%" * 80
    print " Running all tests..."
    print "%" * 80
    print ""

    test_lint()
    test_django()
    test_e2e()


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
                _print("Dropping database...")
                local('rm sqlite_database')
                print "done"
            elif database_engine == 'django.db.backends.postgresql_psycopg2':
                _print("Dropping database...")
                local('dropdb %s' % database_name)
                print "done"

                _print("Creating database...")
                local('createdb %s' % database_name)
                print "done"

            _print("Syncdb and migrate...")
            local('python manage.py syncdb --noinput')
            local('python manage.py migrate')
            print "done"

            _print("Initialize repo with data...")
            local('python manage.py generate_data')
            print "done"
