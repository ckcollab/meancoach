# meancoach

`git clone https://github.com/dev-coop/meancoach.git`

`cd meancoach/meancoach_project`

Copy `settings/local.py.example` to `settings/local.py`

`pip install -r requirements/base.pip`

`bower install`

`fab fresh_db`

`python manage.py runserver`

# Run tests

From `meancoach/meancoach_project` dir

`pip install -r requirements/dev.pip`

`fab test`
