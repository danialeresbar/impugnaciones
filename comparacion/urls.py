from django.urls import path, include
from . import views


urlpatterns = [
    path("comparacion/votacion/", views.votacionListView.as_view(), name="comparacion_votacion_list"),
    path("comparacion/votacion/create/", views.votacionCreateView.as_view(), name="comparacion_votacion_create"),
    path("comparacion/votacion/detail/<int:pk>/", views.votacionDetailView.as_view(), name="comparacion_votacion_detail"),
    path("comparacion/votacion/update/<int:pk>/", views.votacionUpdateView.as_view(), name="comparacion_votacion_update"),
    path('cparroquia-autocomplete/', views.CParroquiaAutocomplete.as_view(), name='cparroquia-autocomplete', ),
    path('czona-autocomplete/', views.CZonaAutocomplete.as_view(), name='czona-autocomplete', ),
    path('ccanton-autocomplete/', views.CCantonAutocomplete.as_view(), name='ccanton-autocomplete', ),
    path('cprovincia-autocomplete/', views.CProvinciaAutocomplete.as_view(), name='cprovincia-autocomplete', ),
    path('uprovincia-autocomplete/', views.UProvinciaAutocomplete.as_view(), name='uprovincia-autocomplete', ),
    path('consulta_presidente/<str:pk_test>/', views.Consulta_presidente, name="consulta_presidente"),
    path('consulta_asamblea_nacional/<str:pk_test>/', views.Consulta_Nacional, name="consulta_asamblea_nacional"),
    path('consulta_asamblea_provincial/<str:pk_test>/', views.Consulta_Provincial, name="consulta_asamblea_provincial"),
    path('consulta_andino/<str:pk_test>/', views.Consulta_Andino, name="consulta_andino"),
    path('incidencias/<str:pk_test>/', views.Incidencias, name="incidencias_presidente"),
    path('read/<str:pk>', views.VotacionModalView, name='read_book'),
    path('validacion_presidente/<str:pk_test>/', views.Validacion_presidente, name="validacion_presidente"),
    path('validacion_asamblea_nacional/<str:pk_test>/', views.Validacion_asambleanacional, name="validacion_asamblea_nacional"),
    path('validacion_asamblea_provincial/<str:pk_test>/', views.Validacion_asambleaprovincial,name="validacion_asamblea_provincial"),
    path('validacion_andino/<str:pk_test>/', views.Validacion_andino,name="validacion_andino"),
    path('excel_presidente/<str:pk_test>/', views.Excel_Presidente, name='excel_presidente'),
    path('excel_asamblea_nacional/<str:pk_test>/', views.Excel_Asamblea_Nacional, name='excel_asamblea_nacional'),
    path('excel_asamblea_provincial/<str:pk_test>/', views.Excel_Asamblea_Provincial, name='excel_asamblea_provincial'),
    path('excel_andino/<str:pk_test>/', views.Excel_Andino, name='excel_andino'),
    path('validar/<str:pk>', views.JRVView, name='validar_jrv'),
    path('validar_nacional/<str:pk>', views.JRVViewnal, name='validar_nacional'),
    path('validar_provincial/<str:pk>', views.JRVViewprov, name='validar_provincial'),
    path('validar_andino/<str:pk>', views.JRVViewand, name='validar_andino'),
    path('editar_incidencia/<str:pk>', views.JRVViewIncidencia, name='edit_jrv_incidencia'),
]
