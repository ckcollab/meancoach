from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('meancoach.urls', namespace='meancoach')),
    url(r'^metrics/', include('metrics.urls', namespace='metrics')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
