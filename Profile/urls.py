from django.urls import path
from .views import ProfileslViewSet, ProfilesApi, ProfilesUpdateApi, ProfilesDeleteApi
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('profile/',ProfilesApi.as_view()),
    path('profile/create/',ProfileslViewSet.as_view()),
    path('profile/<int:pk>/',ProfilesUpdateApi.as_view()),
    path('profile/<int:pk>/delete/',ProfilesDeleteApi.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)