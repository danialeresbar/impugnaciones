from autenticacion.views import index, login_view
from django.urls import path


urlpatterns = [
    path('login/', login_view, name="login"),
    path('', index, name='home'),
]
