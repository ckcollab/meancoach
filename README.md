# meancoach

1. `git clone https://github.com/dev-coop/meancoach.git`

2. `cd meancoach/meancoach_project`

3. `cp settings/local.py.example settings/local.py` and change your `SECRET_KEY`

4. `pip install -r requirements/base.pip`

5. `bower install`

6. `fab fresh_db`

7. `python manage.py runserver`

8. [http://localhost:8000/](http://localhost:8000/) for your new server!

# Run tests

From `meancoach/meancoach_project` dir

`pip install -r requirements/dev.pip`

`fab test`
