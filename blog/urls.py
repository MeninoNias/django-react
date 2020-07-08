from django.urls import include
from rest_framework import routers
from .views import GroupViewSet, UserViewSet
from core.views import ListViewSet, ItemViewSet
from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lists', ListViewSet, basename='list')
router.register(r'itens', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
]
