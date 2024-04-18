from django.apps import AppConfig


class CameraFilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Camera_Files'

    def ready(self):
        import Camera_Files.signals