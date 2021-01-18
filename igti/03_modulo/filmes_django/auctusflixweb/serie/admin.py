"""Aqui acontece o registro do modelo para depois migrá-lo para aplicação."""
from django.contrib import admin
from serie.models import Serie

# Register your models here.
admin.site.register(Serie)
