# coding: utf-8

from django.contrib.gis.db import models


# Regra de instrospecção necessária para o South trabalhar com o GeoDjango
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis\.db\.models\.PointField"])


class Ponto(models.Model):

    nome = models.CharField(max_length=100, blank=True)
    ref = models.CharField(max_length=15, blank=True)
    osmid = models.CharField(max_length=15, unique=True)
    location = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s' % self.id


class Avaliacao(models.Model):

    OPCOES = (
        ('favoravel', 'Favorável'),
        ('aceitavel', 'Aceitável'),
        ('critica', 'Crítica'),
        )

    ponto = models.OneToOneField('Ponto')
    acesso = models.CharField("Condição de Acesso",
                                choices=OPCOES,
                                max_length=10)
    acesso_desc = models.TextField("Justificativa Acesso")

    abrigo = models.CharField("Condição do Abrigo",
                                choices=OPCOES,
                                max_length=10)
    abrigo_desc = models.TextField("Justificativa Abrigo")

    piso = models.CharField("Condição do Piso",
                                choices=OPCOES,
                                max_length=10)
    piso_desc = models.TextField("Justificativa Piso")

    rampa = models.CharField("Condição das Rampas",
                                choices=OPCOES,
                                max_length=10)
    rampa_desc = models.TextField("Justificativa Rampas")

    calcada = models.CharField("Condição das Calçadas",
                                choices=OPCOES,
                                max_length=10)
    calcada_desc = models.TextField("Justificativa Calçada")

    plataforma = models.CharField("Condição das Plataformas",
                                choices=OPCOES,
                                max_length=10)
    plataforma_desc = models.TextField("Justificativa Plataformas")

    transito = models.CharField("Condição do Trânsito de Usuários",
                                choices=OPCOES,
                                max_length=10)
    transito_desc = models.TextField("Justificativa Trânsito")

    equipamento = models.CharField("Condição dos Equipamentos",
                                choices=OPCOES,
                                max_length=10)
    equipamento_desc = models.TextField("Justificativa Equipamentos")

    identificacao = models.CharField("Condição de Identificação",
                                choices=OPCOES,
                                max_length=10)
    identificacao_desc = models.TextField("Justificativa Identificação")

    piso_tatil = models.CharField("Condição do Piso Tátil",
                                choices=OPCOES,
                                max_length=10)
    piso_tatil_desc = models.TextField("Justificativa Piso Tátil")

    linhas = models.CharField("Condição de Identificação das Linhas de Ônibus",
                                choices=OPCOES,
                                max_length=10)
    linhas_desc = models.TextField("Justificativa Identificação das Linhas")

    logradouro = models.CharField("Condição de Identificação do Logradouro",
                                choices=OPCOES,
                                max_length=10)
    logradouro_desc = models.TextField("Justificativa Logradouro")
    objects = models.GeoManager()

    def __unicode__(self):
        return 'Avaliação do Ponto %s' % self.ponto

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"