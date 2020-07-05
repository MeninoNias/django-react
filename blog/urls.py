from django.urls import include, path
from rest_framework import routers
from .views import GroupViewSet, UserViewSet
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
