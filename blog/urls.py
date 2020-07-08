from django.urls import include
from rest_framework import routers
from .views import GroupViewSet, UserViewSet
from core.views import ListViewSet, ItemViewSet
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lists', ListViewSet, basename='list')
router.register(r'itens', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
