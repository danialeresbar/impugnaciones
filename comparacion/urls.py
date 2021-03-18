from django.urls import path
from . import views


urlpatterns = [
    # path("comparacion/votacion/", views.votacionListView.as_view(), name="comparacion_votacion_list"),
    # path("comparacion/votacion/create/", views.votacionCreateView.as_view(), name="comparacion_votacion_create"),
    # path(
    #     "comparacion/votacion/detail/<int:pk>/",
    #     views.votacionDetailView.as_view(),
    #     name="comparacion_votacion_detail"
    # ),
    # path(
    #     "comparacion/votacion/update/<int:pk>/",
    #     views.votacionUpdateView.as_view(),
    #     name="comparacion_votacion_update"
    # ),
    path('cparroquia-autocomplete/', views.CParroquiaAutocomplete.as_view(), name='cparroquia-autocomplete', ),
    path('czona-autocomplete/', views.CZonaAutocomplete.as_view(), name='czona-autocomplete', ),
    path('ccanton-autocomplete/', views.CCantonAutocomplete.as_view(), name='ccanton-autocomplete', ),
    path('cprovincia-autocomplete/', views.CProvinciaAutocomplete.as_view(), name='cprovincia-autocomplete', ),
    path('uprovincia-autocomplete/', views.UProvinciaAutocomplete.as_view(), name='uprovincia-autocomplete', ),
    path('consulta_presidente/<str:pk_test>/', views.Consulta_presidente, name="consulta_presidente"),
    path('incidencias/<str:pk_test>/', views.Incidencias, name="incidencias_presidente"),
    path('read/<str:pk>', views.VotacionModalView, name='read_book'),
    path('validacion_presidente/<str:pk_test>/', views.Validacion_presidente, name="validacion_presidente"),
    path('excel_presidente/<str:pk_test>/', views.Excel_Presidente, name='excel_presidente'),
    path('validar/<str:pk>', views.JRVView, name='validar_jrv'),
    path('editar_incidencia/<str:pk>', views.JRVViewIncidencia, name='edit_jrv_incidencia'),
]
