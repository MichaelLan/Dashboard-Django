from django.contrib import admin
from .models import Proyecto

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('localidad', 'proyecto', 'tipo_proyecto', 'created')
    list_filter = ('localidad', 'tipo_proyecto')

admin.site.register(Proyecto, ProyectoAdmin)