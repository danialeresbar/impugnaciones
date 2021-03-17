import os
import sys
from time import time
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from comparacion.models import votacion
from estructura.models import partido, JRV
from django.db.models import Q


# ---------CREACION DE UIDS----------
def create_jrv_candidato():
    jrvs = JRV.objects.all()
    votacionbulk = []
    uidpartidos = partido.objects.all()
    nacionalpartidos = uidpartidos.filter(Q(dignidad=1))
    for jrv in jrvs:
        for nacionalpartido in nacionalpartidos:
            uidcod = jrv.cod + "{:02d}".format(nacionalpartido.dignidad.pk) + "{:04d}".format(int(nacionalpartido.codpartido))
            votacionbulk.append(
                votacion(
                    provincia=jrv.provincia, canton=jrv.canton,
                    parroquia=jrv.parroquia, zona=jrv.zona, recinto=jrv.recinto,
                    dignidad=nacionalpartido.dignidad, partido=nacionalpartido, jrv=jrv, cod=uidcod
                )
            )
        votacion.objects.bulk_create(votacionbulk)
        votacionbulk.clear()
        provincialpartidos = uidpartidos.filter(dignidad=7, provincia=jrv.provincia)
        for provincialpartido in provincialpartidos:
            uidcod = jrv.cod + "{:02d}".format(provincialpartido.dignidad.pk) + "{:04d}".format(int(provincialpartido.codpartido))
            votacionbulk.append(votacion(provincia=jrv.provincia, canton=jrv.canton,
                       parroquia=jrv.parroquia, zona=jrv.zona, recinto=jrv.recinto,
                       dignidad=provincialpartido.dignidad,  partido=provincialpartido, jrv=jrv, cod=uidcod))
        votacion.objects.bulk_create(votacionbulk)
        votacionbulk.clear()


start_time = time()
create_jrv_candidato()
elapsed_time = time() - start_time
print(f'Elapsed time: {elapsed_time} seconds')
