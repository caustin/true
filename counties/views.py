from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views import generic
from django.shortcuts import get_object_or_404
from counties.models import CountyInfo


class CountyListView(generic.ListView):
    """Generic ListView for CountyInfo models."""

    template_name = "county_index.html"
    context_object_name = "county_list"
    paginate_by = 20

    def get_queryset(self):
        """Overriding the base method to generate a specific queryset"""

        return CountyInfo.objects.order_by('county_name', 'name')

@login_required
def get_detail(request, pk):

    county_name = get_object_or_404(CountyInfo, pk=pk).county_name
    county_infos = CountyInfo.objects.filter(county_name=county_name)

    res = {
        'county_name': county_infos[0].county_name,
    }

    # This is probably a sub-optimal hack but it is most-likely due to the way
    # the data is de-normalized.  Come back to this after the data is normalized.
    cities = []
    for o in county_infos:
        cities.append(
            {
                'name': o.name,
                "latitude": o.primary_latitude,
                'longitude': o.primary_longitude
            }
        )

    res['cities'] = cities

    return render_to_response('county_detail.html', {'county_name': county_name, "county_infos": county_infos})