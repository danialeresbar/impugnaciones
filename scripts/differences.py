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


class AlertManager:
    """

    """

    @classmethod
    def unes_cne_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (pusieron, para_validar, unes_cne_alert) = (cne_lasso - app_lasso, TRUE, TRUE)  WHERE cne_lasso - app_lasso > 0")
            cursor.execute("UPDATE estructura_jrv SET (quitaron, para_validar, unes_cne_alert) = (app_arauz - cne_arauz, TRUE, TRUE)  WHERE  app_arauz - cne_arauz > 0 ")
            cursor.execute("SELECT * FROM estructura_jrv WHERE unes_cne_alert = TRUE")
            for row in cursor.fetchall():
                print(row)

    @classmethod
    def non_suffragettes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar, suffragettes_alert) = (TRUE, TRUE) WHERE cnesufragantes = 0 ")
            cursor.execute("SELECT * FROM estructura_jrv WHERE suffragettes_alert = TRUE")
            for row in cursor.fetchall():
                print(row)

    @classmethod
    def total_votes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar, suffragettes_votes_alert) = (TRUE, TRUE) WHERE cnesufragantes > 350")
            cursor.execute("SELECT * FROM estructura_jrv WHERE suffragettes_votes_alert = TRUE")
            for row in cursor.fetchall():
                print(row)

    @classmethod
    def arauz_votes_alert(cls):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE estructura_jrv SET (para_validar, arauz_votes_alert) = (TRUE, TRUE) WHERE cne_arauz = 0")
            cursor.execute("SELECT * FROM estructura_jrv WHERE arauz_votes_alert = TRUE")
            for row in cursor.fetchall():
                print(row)


# ---------CREACION DE UIDS----------
# TODO: check this method
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


print("----------UNES-CNE Alert----------")
AlertManager.unes_cne_alert()
print("----------Total-Votes Alert----------")
AlertManager.total_votes_alert()
print("----------Arauz-Votes Alert----------")
AlertManager.arauz_votes_alert()
print("----------Non-Suffragettes Alert----------")
AlertManager.non_suffragettes_alert()
