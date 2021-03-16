# from dal import forward
# from dal_admin_filters import AutocompleteFilter

from django import forms
from django.contrib import admin

from estructura import models


# class estructura_ParroquiaFilter(AutocompleteFilter):
#     title = 'Parroquia'                    # filter's title
#     field_name = 'parroquia'           # field name - ForeignKey to Country model
#     autocomplete_url = 'gparroquia-autocomplete' # url name of Country autocomplete view
#
#
# class estructura_ZonaFilter(AutocompleteFilter):
#     title = 'Zona'                    # filter's title
#     field_name = 'zona'           # field name - ForeignKey to Country model
#     autocomplete_url = 'gzona-autocomplete' # url name of Country autocomplete view
#
#
# class estructura_CantonFilter(AutocompleteFilter):
#     title = 'Canton'                    # filter's title
#     field_name = 'canton'           # field name - ForeignKey to Country model
#     autocomplete_url = 'gcanton-autocomplete' # url name of Country autocomplete view
#
# class estructura_ProvinciaFilter(AutocompleteFilter):
#     title = 'Provincia'                    # filter's title
#     field_name = 'provincia'           # field name - ForeignKey to Country model
#     autocomplete_url = 'gprovincia-autocomplete' # url name of Country autocomplete view
#
#
# class estructura_zonaForwardFilter(AutocompleteFilter):
#     autocomplete_url = 'gzona-autocomplete'
#     title = 'Zona'
#     field_name = 'zona'
#     forwards = [
#         forward.Field(
#             'parroquia__id__exact',  # Field name of filter input
#             'parroquia'  # Field name passed to the autocomplete_url endpoint
#         )
#     ]
#     print(estructura_ParroquiaFilter.forwards)


class RecintoAdminForm(forms.ModelForm):
    class Meta:
        model = models.Recinto
        fields = "__all__"


class RecintoAdmin(admin.ModelAdmin):
    form = RecintoAdminForm
    list_display = ('codrecinto', 'nomrecinto')
    readonly_fields = ('codrecinto', 'nomrecinto')
    list_filter = ('parroquia', 'zona__nomzona')
    search_fields = ('nomrecinto',)


class CantonAdminForm(forms.ModelForm):

    class Meta:
        model = models.Canton
        fields = "__all__"


class CantonAdmin(admin.ModelAdmin):
    form = CantonAdminForm
    list_display = ('nomcanton', 'codcanton')
    readonly_fields = ('nomcanton', 'codcanton')
    list_filter = ('provincia',)
    search_fields = ('nomcanton',)


class ZonaAdminForm(forms.ModelForm):
    class Meta:
        model = models.Zona
        fields = "__all__"


class ZonaAdmin(admin.ModelAdmin):
    form = ZonaAdminForm
    list_display = ('nomzona', 'codzona')
    readonly_fields = ('nomzona', 'codzona')
    list_filter = ('parroquia',)
    search_fields = ('nomzona',)


class ParroquiaAdminForm(forms.ModelForm):
    class Meta:
        model = models.Parroquia
        fields = "__all__"


class ParroquiaAdmin(admin.ModelAdmin):
    form = ParroquiaAdminForm
    list_display = ('codparroquia', 'nomparroquia')
    readonly_fields = ('codparroquia', 'nomparroquia')
    list_filter = ('canton',)
    search_fields = ('nomparroquia',)


class ProvinciaAdminForm(forms.ModelForm):
    class Meta:
        model = models.Provincia
        fields = "__all__"


class ProvinciaAdmin(admin.ModelAdmin):
    form = ProvinciaAdminForm
    list_display = ('codprovincia', 'nomprovincia')
    readonly_fields = ('codprovincia', 'nomprovincia')
    search_fields = ('nomprovincia',)


class JRVAdminForm(forms.ModelForm):
    class Meta:
        model = models.JRV
        fields = "__all__"


class JRVAdmin(admin.ModelAdmin):
    form = JRVAdminForm
    list_display = ('cod',)
    readonly_fields = ('acta_cne',)


class PartidoAdminForm(forms.ModelForm):
    class Meta:
        model = models.partido
        fields = "__all__"


class PartidoAdmin(admin.ModelAdmin):
    form = PartidoAdminForm
    list_display = ('nompartido', 'codpartido')
    readonly_fields = ('nompartido', 'codpartido')
    search_fields = ('nompartido',)


class DignidadAdminForm(forms.ModelForm):
    class Meta:
        model = models.dignidad
        fields = "__all__"


class DignidadAdmin(admin.ModelAdmin):
    form = DignidadAdminForm
    list_display = ('coddignidad', 'nomdignidad')
    readonly_fields = ('coddignidad', 'nomdignidad')
    search_fields = ('nomdignidad',)


admin.site.register(models.Provincia, ProvinciaAdmin)
admin.site.register(models.Canton, CantonAdmin)
admin.site.register(models.Zona, ZonaAdmin)
admin.site.register(models.Parroquia, ParroquiaAdmin)
admin.site.register(models.Recinto, RecintoAdmin)
admin.site.register(models.JRV, JRVAdmin)
admin.site.register(models.partido, PartidoAdmin)
admin.site.register(models.dignidad, DignidadAdmin)
