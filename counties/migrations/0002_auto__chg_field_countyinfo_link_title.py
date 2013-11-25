# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CountyInfo.link_title'
        db.alter_column(u'counties_countyinfo', 'link_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CountyInfo.link_title'
        raise RuntimeError("Cannot reverse this migration. 'CountyInfo.link_title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CountyInfo.link_title'
        db.alter_column(u'counties_countyinfo', 'link_title', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'counties.countyinfo': {
            'Meta': {'object_name': 'CountyInfo'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'feat_class': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'feature_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'fips_class': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fips_county_cd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_county_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'primary_longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['counties']