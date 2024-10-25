from django.contrib import admin

# Register your models here.
from django.apps import apps

app = apps.get_app_config('cv')

for model in app.get_models():
    admin.site.register(model)
