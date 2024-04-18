"""
URL configuration for hut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include ,re_path
from account import api
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # re_path(r'^admin/', admin.site.urls),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('account/', include('account.urls')),
    path('Profile/' , include('Profile.urls')),
    path('Camera_Files/' , include('Camera_Files.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
