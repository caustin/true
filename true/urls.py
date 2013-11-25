from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

import counties.urls

from true.views import MyRegistrationView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls', namespace="counties")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^counties/', include(counties.urls)),
    url(r'^register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', RedirectView.as_view(url='/counties/')),
)


