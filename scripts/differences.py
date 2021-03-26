import os
import sys
import django
from django.db import connection

# For Docker container
sys.path.append('/src')
# For production server
sys.path.append('/home/administrator/impugnaciones')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from estructura.models import Alert, JRV


class AlertManager:
    """

    """

    ALERTS = {index: alert for index, alert in enumerate(Alert.objects.all())}

    @classmethod
    def unes_cne_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (quitaron, para_validar) = (cne_arauz - app_arauz, True)  WHERE  cne_arauz - app_arauz <> 0 ")
            cursor.execute("UPDATE estructura_jrv SET (quitaron, para_validar) = (cne_lasso - app_lasso, True)  WHERE cne_lasso - app_lasso <> 0")
            # TODO: Obtener los registros modificados para asignar la respectiva alerta

    @classmethod
    def non_suffragettes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar) = (True) WHERE cnesufragantes < 0 ")
            # TODO: Obtener los registros modificados para asignar la respectiva alerta

    @classmethod
    def total_votes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar) = (True) WHERE cne_arauz + app_arauz > 350")
            # TODO: Obtener los registros modificados para asignar la respectiva alerta

    @classmethod
    def arauz_votes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar) = (True) WHERE cne_arauz + app_arauz < 0")
            # TODO: Obtener los registros modificados para asignar la respectiva alerta


# ---------CREACION DE UIDS----------
def get_diffs():
    pass
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


AlertManager.unes_cne_alert()
# get_diffs()
