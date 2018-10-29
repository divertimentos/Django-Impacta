from django.contrib import admin
from django.urls import path
from core import views
# from core.views import *

urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro),
    path('admin/', admin.site.urls),
]
