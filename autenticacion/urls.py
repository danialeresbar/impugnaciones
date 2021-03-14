from autenticacion.views import index, login_view, register_user
from django.urls import path, re_path

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', index, name='home'),
]
