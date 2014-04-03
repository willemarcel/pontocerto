# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Ponto', fields ['nome']
        db.delete_unique('core_ponto', ['nome'])

        # Removing unique constraint on 'Ponto', fields ['ref']
        db.delete_unique('core_ponto', ['ref'])


    def backwards(self, orm):
        # Adding unique constraint on 'Ponto', fields ['ref']
        db.create_unique('core_ponto', ['ref'])

        # Adding unique constraint on 'Ponto', fields ['nome']
        db.create_unique('core_ponto', ['nome'])


    models = {
        'core.avaliacao': {
            'Meta': {'object_name': 'Avaliacao'},
            'abrigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abrigo_desc': ('django.db.models.fields.TextField', [], {}),
            'acesso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'acesso_desc': ('django.db.models.fields.TextField', [], {}),
            'calcada': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'calcada_desc': ('django.db.models.fields.TextField', [], {}),
            'equipamento': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'equipamento_desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacao': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'identificacao_desc': ('django.db.models.fields.TextField', [], {}),
            'linhas': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'linhas_desc': ('django.db.models.fields.TextField', [], {}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'logradouro_desc': ('django.db.models.fields.TextField', [], {}),
            'piso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piso_desc': ('django.db.models.fields.TextField', [], {}),
            'piso_tatil': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piso_tatil_desc': ('django.db.models.fields.TextField', [], {}),
            'plataforma': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'plataforma_desc': ('django.db.models.fields.TextField', [], {}),
            'ponto': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Ponto']"}),
            'rampa': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rampa_desc': ('django.db.models.fields.TextField', [], {}),
            'transito': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'transito_desc': ('django.db.models.fields.TextField', [], {})
        },
        'core.ponto': {
            'Meta': {'object_name': 'Ponto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'osmid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['core']