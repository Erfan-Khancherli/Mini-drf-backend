from django.urls import path
from .views import Camera_FileslViewSet, Camera_FilesApi, Camera_FilesUpdateApi, Camera_FilesDeleteApi , GtokenViewSet

urlpatterns = [
    path('files/',Camera_FilesApi.as_view()),
    path('files/create/',Camera_FileslViewSet.as_view()),
    path('files/<int:pk>/',Camera_FilesUpdateApi.as_view()),
    path('files/<int:pk>/delete/',Camera_FilesDeleteApi.as_view()),
    path('getgtoken/' , GtokenViewSet.as_view())
]