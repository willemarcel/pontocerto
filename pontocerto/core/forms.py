# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Comentario


class ComentarioForm(ModelForm):
    model = Comentario
    exclude = ['data']
