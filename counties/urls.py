from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from counties.views import CountyListView, get_detail


urlpatterns = patterns('',
    url(r'^$',login_required( CountyListView.as_view()), name="index"),
    url(r'^(?P<pk>\d+)/$', get_detail, name="detail"),
)