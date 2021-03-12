from django import forms
from . import models


class RecintoForm(forms.ModelForm):
    class Meta:
        model = models.Recinto
        fields = [
            "codrecinto",
            "nomrecinto",
            "parroquia",
            "zona",
        ]


class CantonForm(forms.ModelForm):
    class Meta:
        model = models.Canton
        fields = [
            "nomcanton",
            "codcanton",
            "provincia",
        ]


class ZonaForm(forms.ModelForm):
    class Meta:
        model = models.Zona
        fields = [
            "nomzona",
            "codzona",
            "parroquia",
        ]


class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = models.Parroquia
        fields = [
            "codparroquia",
            "nomparroquia",
            "canton",
        ]


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = models.Provincia
        fields = [
            "codprovincia",
            "nomprovincia",
        ]
