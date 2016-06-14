# coding: utf-8

from django.contrib.gis.db import models


class Ponto(models.Model):

    nome = models.CharField(max_length=100, blank=True)
    ref = models.CharField(max_length=15, blank=True)
    osmid = models.CharField(max_length=15, unique=True)
    location = models.PointField()
    objects = models.GeoManager()

    def __str__(self):
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

    def final(self):
        resultado = [self.acesso, self.abrigo, self.piso, self.rampa,
            self.calcada, self.plataforma, self.transito, self.equipamento,
            self.identificacao, self.piso_tatil, self. linhas, self.logradouro]
        pontuacao = resultado.count('favoravel') * 2 \
            + resultado.count('aceitavel') * 1

        if pontuacao >= 14:
            return 'favoravel'
        elif pontuacao >= 7:
            return 'aceitavel'
        else:
            return 'critica'

    def __str__(self):
        return 'Avaliação do Ponto %s' % self.ponto

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Comentario(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data = models.DateTimeField(auto_now_add=True)
    ponto = models.ForeignKey(Ponto)
    conteudo = models.TextField()

    def __str__(self):
        return 'Comentário %s' % self.id
