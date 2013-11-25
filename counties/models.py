from django.db import models


class CountyInfo(models.Model):
    """One To One mapping of the 'city_links_for_state_of' results schema.

    The JSON Schema from the 'city_links_for_state_of' is highly de-normalized.
    However, for the sake of expediency, for now this model will match the JSON
    schema and rely on filtering views and forms.
    See http://www.sba.gov/about-sba/sba_performance/sba_data_store/web_service_api/u_s_city_and_county_web_data_api#city-county-state
    for the schema definition.
    """

    county_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    feat_class = models.CharField(max_length=255)
    feature_id = models.IntegerField(max_length=11)
    fips_class = models.CharField(max_length=2)
    fips_county_cd = models.CharField(max_length=255)
    full_county_name = models.CharField(max_length=255)
    link_title = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # Schema documentation calls for a float for these two fields.
    # However, python decimal types have advantages over python's float types
    # so a decimal is being used here in it's stead.  See
    # http://docs.python.org/2.7/library/decimal.html#module-decimal
    # for clarification on decimal vs float.
    primary_latitude = models.DecimalField(decimal_places=2, max_digits=4)
    primary_longitude = models.DecimalField(decimal_places=2, max_digits=5)
    state_abbreviation = models.CharField(max_length=2,)
    state_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name
