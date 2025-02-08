from django.apps import AppConfig
from django.contrib import admin

class AppagriConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'appagri'
	verbose_name = 'UAB Models'

	def ready(self):
		admin.site.index_title = 'UrbanAgriCulture Admin Interface | UAB Admin Site'
