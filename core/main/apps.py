from django.apps import AppConfig


class MainConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "main"

	#load signals when app is initialized
	def ready(self):
		from . import signals
		