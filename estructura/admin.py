from django.contrib import admin
from django import forms
from estructura import models
from dal_admin_filters import AutocompleteFilter
from dal import forward


class estructura_ParroquiaFilter(AutocompleteFilter):
    title = 'Parroquia'                    # filter's title
    field_name = 'parroquia'           # field name - ForeignKey to Country model
    autocomplete_url = 'gparroquia-autocomplete' # url name of Country autocomplete view

class estructura_ZonaFilter(AutocompleteFilter):
    title = 'Zona'                    # filter's title
    field_name = 'zona'           # field name - ForeignKey to Country model
    autocomplete_url = 'gzona-autocomplete' # url name of Country autocomplete view

class estructura_CantonFilter(AutocompleteFilter):
    title = 'Canton'                    # filter's title
    field_name = 'canton'           # field name - ForeignKey to Country model
    autocomplete_url = 'gcanton-autocomplete' # url name of Country autocomplete view

class estructura_ProvinciaFilter(AutocompleteFilter):
    title = 'Provincia'                    # filter's title
    field_name = 'provincia'           # field name - ForeignKey to Country model
    autocomplete_url = 'gprovincia-autocomplete' # url name of Country autocomplete view

class estructura_zonaForwardFilter(AutocompleteFilter):
    autocomplete_url = 'gzona-autocomplete'
    title = 'Zona'
    field_name = 'zona'
    forwards = [
        forward.Field(
            'parroquia__id__exact',  # Field name of filter input
            'parroquia'  # Field name passed to the autocomplete_url endpoint
        )
    ]
    print(estructura_ParroquiaFilter.forwards)

class RecintoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Recinto
        fields = "__all__"

class RecintoAdmin(admin.ModelAdmin):
    form = RecintoAdminForm
    list_display = [
        "codrecinto",
        "nomrecinto",

    ]
    readonly_fields = [
        "codrecinto",
        "nomrecinto",

    ]
    list_filter = [estructura_ParroquiaFilter, estructura_zonaForwardFilter]


class CantonAdminForm(forms.ModelForm):

    class Meta:
        model = models.Canton
        fields = "__all__"


class CantonAdmin(admin.ModelAdmin):
    form = CantonAdminForm
    list_display = [
        "nomcanton",
        "codcanton",
    ]
    readonly_fields = [
        "nomcanton",
        "codcanton",
    ]
    list_filter = [estructura_ProvinciaFilter]


class ZonaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Zona
        fields = "__all__"


class ZonaAdmin(admin.ModelAdmin):
    form = ZonaAdminForm
    list_display = [
        "nomzona",
        "codzona",
    ]
    readonly_fields = [
        "nomzona",
        "codzona",
    ]
    list_filter = [estructura_ParroquiaFilter]

class ParroquiaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Parroquia
        fields = "__all__"


class ParroquiaAdmin(admin.ModelAdmin):
    form = ParroquiaAdminForm
    list_display = [
        "codparroquia",
        "nomparroquia",
    ]
    readonly_fields = [
        "codparroquia",
        "nomparroquia",
    ]
    list_filter = [estructura_CantonFilter]

class ProvinciaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Provincia
        fields = "__all__"


class ProvinciaAdmin(admin.ModelAdmin):
    form = ProvinciaAdminForm
    list_display = [
        "codprovincia",
        "nomprovincia",
    ]
    readonly_fields = [
        "codprovincia",
        "nomprovincia",
    ]

class JRVAdminForm(forms.ModelForm):

    class Meta:
        model = models.JRV
        fields = "__all__"

class JRVAdmin(admin.ModelAdmin):
    form = JRVAdminForm
    list_display = [
        "cod",
    ]
    readonly_fields = [
        "acta_cne",    ]

class partidoAdminForm(forms.ModelForm):

    class Meta:
        model = models.partido
        fields = "__all__"

class partidoAdmin(admin.ModelAdmin):
    form = partidoAdminForm
    list_display = [
        "nompartido",
        "codpartido",
    ]
    readonly_fields = [
        "nompartido",
        "codpartido",
    ]



class dignidadAdminForm(forms.ModelForm):

    class Meta:
        model = models.dignidad
        fields = "__all__"

class dignidadAdmin(admin.ModelAdmin):
    form = dignidadAdminForm
    list_display = [
        "coddignidad",
        "nomdignidad",
    ]
    readonly_fields = [
        "coddignidad",
        "nomdignidad",
    ]


admin.site.register(models.Provincia, ProvinciaAdmin)
admin.site.register(models.Canton, CantonAdmin)
admin.site.register(models.Zona, ZonaAdmin)
admin.site.register(models.Parroquia, ParroquiaAdmin)
admin.site.register(models.Recinto, RecintoAdmin)
admin.site.register(models.JRV, JRVAdmin)
admin.site.register(models.partido, partidoAdmin)
admin.site.register(models.dignidad, dignidadAdmin)
