from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from people.views import PersonViewSet

# Cria o roteador do DRF
router = routers.DefaultRouter()
router.register(r"people", PersonViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),   # rota do Django Admin
    path("api/", include(router.urls)),  # rota da API REST
]