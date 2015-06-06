meancoach [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy) [![Test Coverage](https://codeclimate.com/github/dev-coop/meancoach/badges/coverage.svg)](https://codeclimate.com/github/dev-coop/meancoach/coverage) [![Code Climate](https://codeclimate.com/github/dev-coop/meancoach/badges/gpa.svg)](https://codeclimate.com/github/dev-coop/meancoach) 
=========

1. `git clone https://github.com/dev-coop/meancoach.git`

2. `cd meancoach/meancoach_project`

3. `export DJANGO_SETTINGS_MODULE=settings.local` added to your `postactivate` script

4. `cp settings/local.py.example settings/local.py` and change your `SECRET_KEY`

5. `pip install -r requirements/dev.pip`

6. `bower install`

7. `fab fresh_db`

8. `python manage.py runserver`

9. [http://localhost:8000/](http://localhost:8000/) for your new server!

# Run tests

From `meancoach/meancoach_project` dir

`fab test`
