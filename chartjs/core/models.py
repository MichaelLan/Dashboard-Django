from django.db import models

# Create your models here.
class Proyecto(models.Model):
    localidad = models.CharField(verbose_name ='Localidad', max_length=20)
    proyecto = models.CharField(verbose_name= 'Nombre del proyecto', max_length=70, unique=True)
    tipo_proyecto = models.CharField(verbose_name= 'Tipo de proyecto', max_length=30)
    perfil_1 = models.IntegerField(verbose_name='Perfil 1', default=0)
    perfil_2 = models.IntegerField(verbose_name='Perfil 2', default=0)
    perfil_3 = models.IntegerField(verbose_name='Perfil 3', default=0)
    perfil_4 = models.IntegerField(verbose_name='Perfil 4', default=0)
    perfil_5 = models.IntegerField(verbose_name='Perfil 5', default=0)
    slug_localidad = models.SlugField(verbose_name='Slug Localidad', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.proyecto
