meancoach  
=========

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy) [![Test Coverage](https://codeclimate.com/github/dev-coop/meancoach/badges/coverage.svg)](https://codeclimate.com/github/dev-coop/meancoach/coverage) [![Code Climate](https://codeclimate.com/github/dev-coop/meancoach/badges/gpa.svg)](https://codeclimate.com/github/dev-coop/meancoach)

```git clone https://github.com/dev-coop/meancoach.git```

```cd meancoach/meancoach_project```

Add ```export DJANGO_SETTINGS_MODULE=settings.local``` to your `postactivate` script


```cp settings/local.py.example settings/local.py```

```pip install -r requirements/dev.pip```

```bower install && npm install -g stylus```

```fab fresh_db```

```python manage.py runserver```

[http://localhost:8000/](http://localhost:8000/) for your new server!


# Run tests

From `meancoach/meancoach_project` dir

`fab test`
