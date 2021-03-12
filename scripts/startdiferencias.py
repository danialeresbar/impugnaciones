import os
import sys
import django

sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from comparacion.models import votacion
from django.db import connection


# ---------CREACION DE UIDS----------
def get_diffs():
    cursor = connection.cursor()
    cursor.execute(
        "update comparacion_votacion set diff1 = cne1 - delegados  where delegados is not null and cne1 - delegados <> 0 ")
    cursor.execute(
        "update comparacion_votacion set diff2 = cne1 - app_digitacion  where app_digitacion is not null and cne1 - app_digitacion <> 0 ")
    newfile = open('basicos/diferencias.csv', 'w')
    uidJRVDigpartidos = votacion.objects.raw(
        'select * from comparacion_votacion where diff1 is not null or diff2 is not null'
    )

    for uid in uidJRVDigpartidos:
        if uid.zona is None:
            zona = "0"
        else:
            zona = str(uid.zona.codzona)

        line = str(uid.provincia.codprovincia) + "," + str(uid.canton.codcanton) + "," + \
               str(uid.parroquia.codparroquia) + "," + zona + "," + str(uid.recinto.codrecinto) + "," + \
               str(uid.jrv.numero) + "," + uid.jrv.genero + "," + str(uid.dignidad.coddignidad) + "," + \
               str(uid.partido.codpartido) + "," + str(uid.cne1) + "," + str(uid.diff1) + "," + str(uid.diff2) + "\n"
        newfile.write(line)
    newfile.close()


get_diffs()
