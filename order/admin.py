from django.contrib import admin
from django.apps import apps

order_models = apps.get_app_config('order').get_models()
for model in order_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass