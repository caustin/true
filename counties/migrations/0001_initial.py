# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountyInfo'
        db.create_table(u'counties_countyinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('feat_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('feature_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('fips_class', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fips_county_cd', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_county_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('primary_latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('primary_longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('state_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'counties', ['CountyInfo'])


    def backwards(self, orm):
        # Deleting model 'CountyInfo'
        db.delete_table(u'counties_countyinfo')


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
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'primary_longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['counties']