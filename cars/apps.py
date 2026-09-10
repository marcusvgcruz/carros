from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #adicionada manualmente
    name = 'cars'

    def ready(self):
        import cars.signals
