from . import models
from estructura.models import  Provincia, Canton, Recinto
from dal import autocomplete
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm


class votacionForm(forms.ModelForm):

    class Meta:
        model = models.votacion
        fields = [
        "cod",
        "cne1"
        ]


class fantasmaForm(forms.ModelForm):
    class Meta:
        model = models.votacion
        fields = [
        ]

class VotacionModelForm(BSModalModelForm):
    class Meta:
        model = models.votacion
        fields = [
            "cne1"
        ]
