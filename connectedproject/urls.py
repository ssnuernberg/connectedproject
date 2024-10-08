"""
URL configuration for connectedproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from connectedapp.views import CustomUserViewSet, CourseViewSet, FeedbackViewSet, NotificationViewSet, RoleViewSet, StatusViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = [
    path('', include('connectedapp.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
