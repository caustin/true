"""Tools to load the json data file into the db.  Again, for simplicity and
expediency we are using the the models serializer methods.
"""

import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "true.settings")

from counties.models import CountyInfo


def deserialize_json_file():
    """Function to deserialize the county data.

    This is not the most efficient way of loading bulk data but given that the
    data was a JSON file and timeline this method is sufficient for now.
    """

    jd = open("CA.json").read()
    data = json.loads(jd)

    for o in data:
        c = CountyInfo()
        c.link_title = o["link_title"]
        c.county_name = o["county_name"]
        c.description = o['description']
        c.feat_class = o['feat_class']
        c.feature_id = o['feature_id']
        c.county_name = o['county_name']
        c.fips_class = o['fips_class']
        c.fips_county_cd = o['fips_county_cd']
        c.full_county_name = o['full_county_name']
        c.name = o['name']
        c.primary_latitude = o['primary_latitude']
        c.primary_longitude = o['primary_longitude']
        c.state_abbreviation = o['state_abbreviation']
        c.state_name = o['state_name']
        c.url = o['url']

        c.save()

if __name__ == "__main__":
    deserialize_json_file()