# meancoach

1) `git clone https://github.com/dev-coop/meancoach.git`

2) `cd meancoach/meancoach_project`

3) Copy `settings/local.py.example` to `settings/local.py`

4) `pip install -r requirements/base.pip`

5) `bower install`

6) `fab fresh_db`

7) `python manage.py runserver`

# Run tests

From `meancoach/meancoach_project` dir

`pip install -r requirements/dev.pip`

`fab test`
