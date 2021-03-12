
from .views import login_view, register_user

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', views.index, name='home'),
]

