import os
import csv
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","chartjs.settings")
import django, random as ran
from random import random

django.setup()

from core.models import Proyecto

info = []
arch = 'chartjs\infoBD.csv'

with open(arch, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        info.append(row)

info.pop(0)

def poblacion():
    cont = 0
    for i in info:
        cont += 1
        localidad = i[0]
        proyecto = i[1]
        tipo_de_proyecto = i[2]
        perfil_1 = i[3]
        perfil_2 = i[4]
        perfil_3 = i[5]
        perfil_4 = i[6]
        perfil_5 = i[7]


        dato = Proyecto.objects.get_or_create(localidad = localidad, proyecto = proyecto, tipo_proyecto = tipo_de_proyecto, 
                                            perfil_1 = perfil_1, perfil_2 = perfil_2, perfil_3 = perfil_3, 
                                            perfil_4 = perfil_4, perfil_5 = perfil_5)[0]
        dato.save()

        print("Iteración Nº :"+str(cont))

if __name__ == "__main__":
    poblacion()

