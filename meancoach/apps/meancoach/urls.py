from django.conf.urls import url

from apps.meancoach.views import IndexPage


urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
]
