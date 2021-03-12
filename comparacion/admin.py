from django.contrib import admin
from django import forms
from comparacion import models
from django.utils.html import format_html

from dal_admin_filters import AutocompleteFilter
from dal import forward


class comp_ParroquiaFilter(AutocompleteFilter):
    title = 'Parroquia'                    # filter's title
    field_name = 'parroquia'           # field name - ForeignKey to Country model
    autocomplete_url = 'cparroquia-autocomplete' # url name of Country autocomplete view

class comp_ZonaFilter(AutocompleteFilter):
    title = 'Zona'                    # filter's title
    field_name = 'zona'           # field name - ForeignKey to Country model
    autocomplete_url = 'czona-autocomplete' # url name of Country autocomplete view

class comp_CantonFilter(AutocompleteFilter):
    title = 'Canton'                    # filter's title
    field_name = 'canton'           # field name - ForeignKey to Country model
    autocomplete_url = 'ccanton-autocomplete' # url name of Country autocomplete view

class comp_ProvinciaFilter(AutocompleteFilter):
    title = 'Provincia'                    # filter's title
    field_name = 'provincia'           # field name - ForeignKey to Country model
    autocomplete_url = 'cprovincia-autocomplete' # url name of Country autocomplete view


class comp_cantonForwardFilter(AutocompleteFilter):
    autocomplete_url = 'ccanton-autocomplete'
    title = 'Canton'
    field_name = 'canton'
    forwards = [
        forward.Field(
            'provincia__id__exact',  # Field name of filter input
            'provincia'  # Field name passed to the autocomplete_url endpoint
        )
    ]
    print(comp_ParroquiaFilter.forwards)


class comp_parroquiaForwardFilter(AutocompleteFilter):
    autocomplete_url = 'cparroquia-autocomplete'
    title = 'Parroquia'
    field_name = 'parroquia'
    forwards = [
        forward.Field(
            'canton__id__exact',  # Field name of filter input
            'canton'  # Field name passed to the autocomplete_url endpoint
        )
    ]
    print(comp_ParroquiaFilter.forwards)

class comp_zonaForwardFilter(AutocompleteFilter):
    autocomplete_url = 'czona-autocomplete'
    title = 'Zona'
    field_name = 'zona'
    forwards = [
        forward.Field(
            'parroquia__id__exact',  # Field name of filter input
            'parroquia'  # Field name passed to the autocomplete_url endpoint
        )
    ]
    print(comp_ParroquiaFilter.forwards)

class votacionAdminForm(forms.ModelForm):

    class Meta:
        model = models.votacion
        fields = "__all__"


class votacionAdmin(admin.ModelAdmin):
    form = votacionAdminForm

    class Media:
        css = {
            'all': ("styles.css",)
        }
    list_display = [
         "codigo_JRV_Partido",


    ]

    readonly_fields = [
        "cod",
        "codigo_JRV_Partido",

    ]

    def codigo_JRV_Partido(self, instance):
        return format_html(
            '<span class="por_Definir" title="{}">{}</span>',
            "Informacion de la JRV:\n"  +
            "Provincia  " + str(instance.provincia.COD_PROVINCIA) + " - " + instance.provincia.NOM_PROVINCIA +
            "Canton:    " + str(instance.canton.COD_CANTON) + " - " +instance.canton.NOM_CANTON +
            "Parroquia: " + str(instance.parroquia.COD_PARROQUIA) + " - " +instance.parroquia.NOM_PARROQUIA+
            "Zona:      " + str(instance.zona.COD_ZONA) + " - " +instance.zona.NOM_ZONA + "\n"+
            "Recinto:   " + instance.recinto.NOM_RECINTO +"\n"+
            "JRV:       " + str(instance.jrv.numero) + instance.jrv.genero +"\n"+
            "Dignidad:  " + str(instance.dignidad.COD_DIGNIDAD) + " - " + instance.dignidad.NOM_DIGNIDAD +"\n",
            instance.cod
        )

    ordering = ("cod",)

    search_fields = [
        "cod"
    ]

    list_filter = [comp_ProvinciaFilter, comp_cantonForwardFilter, comp_parroquiaForwardFilter, comp_zonaForwardFilter]

class fantasmaAdminForm(forms.ModelForm):

    class Meta:
        model = models.fantasma
        fields = "__all__"


class fantasmaAdmin(admin.ModelAdmin):
    form = fantasmaAdminForm
    list_display = [
        "uid",
    ]
    readonly_fields = [
    ]


admin.site.register(models.votacion, votacionAdmin)
admin.site.register(models.fantasma, fantasmaAdmin)
