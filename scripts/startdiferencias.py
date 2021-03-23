import os
import sys
import django

sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from estructura.models import JRV
from django.db import connection


# ---------CREACION DE UIDS----------
def get_diffs():
    cursor = connection.cursor()
    cursor.execute("update estructura_jrv set quitaron = cne_arauz - app_arauz  where  cne_arauz - app_arauz <> 0 ")
    cursor.execute("update estructura_jrv set quitaron = cne_lasso - app_lasso  where  cne_lasso - app_lasso <> 0")
    cursor.execute("update estructura_jrv set para_validar = True where  cne_arauz - app_arauz <> 0 ")
    cursor.execute("update estructura_jrv set para_validar = True where  cne_lasso - app_lasso <> 0 ")
   #  4%   arreglar sufragantes/votos  ->
   #  cursor.execute("update estructura_jrv set para_validar = True where  cne_arauz - old_cne_arauz <> 0 ")
   # cursor.execute("update estructura_jrv set para_validar = True where  cne_lasso - old_cne_lasso <> 0 ")

    """
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
"""

get_diffs()
