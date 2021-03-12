import sys, os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from comparacion.models import  votacion
from estructura.models import Provincia, Canton, Parroquia,  Zona , Recinto,  dignidad, partido, JRV
from django.db.models import Q
import multiprocessing

#----------------------------------------------------------------------------
#                  CREACION DE UIDS

#-----------------------------------------------------------------------------

class create_JRVCandidato:

    uidJRVs = JRV.objects.all()
    votacionbulk = []
    uidpartidos = partido.objects.all()
    nacionalpartidos = uidpartidos.filter(Q(dignidad=1) | Q(dignidad=8) | Q(dignidad=9))
    for uidJRV in uidJRVs:
        for nacionalpartido in nacionalpartidos:
            uidcod=uidJRV.cod + "{:02d}".format(nacionalpartido.dignidad.pk) +  "{:04d}".format(int(nacionalpartido.codpartido))
            votacionbulk.append(votacion(provincia = uidJRV.provincia, canton = uidJRV.canton,
                       parroquia = uidJRV.parroquia, zona = uidJRV.zona, recinto = uidJRV.recinto,
                       dignidad = nacionalpartido.dignidad,  partido=nacionalpartido, jrv=uidJRV, cod=uidcod))
        votacion.objects.bulk_create(votacionbulk)
        votacionbulk.clear()
        provincialpartidos = uidpartidos.filter(dignidad=7,provincia=uidJRV.provincia)
        for provincialpartido in provincialpartidos:
            uidcod=uidJRV.cod + "{:02d}".format(provincialpartido.dignidad.pk) + "{:04d}".format(int(provincialpartido.codpartido))
            votacionbulk.append(votacion(provincia = uidJRV.provincia, canton = uidJRV.canton,
                       parroquia = uidJRV.parroquia, zona = uidJRV.zona, recinto = uidJRV.recinto,
                       dignidad = provincialpartido.dignidad,  partido=provincialpartido, jrv=uidJRV, cod=uidcod))
        votacion.objects.bulk_create(votacionbulk)
        votacionbulk.clear()





