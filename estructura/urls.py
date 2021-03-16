from django.urls import path

from estructura import views


urlpatterns = (
    path("estructura/Recinto/", views.RecintoListView.as_view(), name="estructura_Recinto_list"),
    path("estructura/Recinto/create/", views.RecintoCreateView.as_view(), name="estructura_Recinto_create"),
    path("estructura/Recinto/detail/<int:pk>/", views.RecintoDetailView.as_view(), name="estructura_Recinto_detail"),
    path("estructura/Recinto/update/<int:pk>/", views.RecintoUpdateView.as_view(), name="estructura_Recinto_update"),
    path("estructura/Canton/", views.CantonListView.as_view(), name="estructura_Canton_list"),
    path("estructura/Canton/create/", views.CantonCreateView.as_view(), name="estructura_Canton_create"),
    path("estructura/Canton/detail/<int:pk>/", views.CantonDetailView.as_view(), name="estructura_Canton_detail"),
    path("estructura/Canton/update/<int:pk>/", views.CantonUpdateView.as_view(), name="estructura_Canton_update"),
    path("estructura/Zona/", views.ZonaListView.as_view(), name="estructura_Zona_list"),
    path("estructura/Zona/create/", views.ZonaCreateView.as_view(), name="estructura_Zona_create"),
    path("estructura/Zona/detail/<int:pk>/", views.ZonaDetailView.as_view(), name="estructura_Zona_detail"),
    path("estructura/Zona/update/<int:pk>/", views.ZonaUpdateView.as_view(), name="estructura_Zona_update"),
    path("estructura/Parroquia/", views.ParroquiaListView.as_view(), name="estructura_Parroquia_list"),
    path("estructura/Parroquia/create/", views.ParroquiaCreateView.as_view(), name="estructura_Parroquia_create"),
    path(
        "estructura/Parroquia/detail/<int:pk>/",
        views.ParroquiaDetailView.as_view(),
        name="estructura_Parroquia_detail"
    ),
    path(
        "estructura/Parroquia/update/<int:pk>/",
        views.ParroquiaUpdateView.as_view(),
        name="estructura_Parroquia_update"
    ),
    path("estructura/Provincia/", views.ProvinciaListView.as_view(), name="estructura_Provincia_list"),
    path("estructura/Provincia/create/", views.ProvinciaCreateView.as_view(), name="estructura_Provincia_create"),
    path(
        "estructura/Provincia/detail/<int:pk>/",
        views.ProvinciaDetailView.as_view(),
        name="estructura_Provincia_detail"
    ),
    path(
        "estructura/Provincia/update/<int:pk>/",
        views.ProvinciaUpdateView.as_view(),
        name="estructura_Provincia_update"
    ),
    path('gparroquia-autocomplete/', views.GParroquiaAutocomplete.as_view(), name='gparroquia-autocomplete', ),
    path('gzona-autocomplete/', views.GZonaAutocomplete.as_view(), name='gzona-autocomplete', ),
    path('gcanton-autocomplete/', views.GCantonAutocomplete.as_view(), name='gcanton-autocomplete', ),
    path('gprovincia-autocomplete/', views.GProvinciaAutocomplete.as_view(), name='gprovincia-autocomplete', ),
)
