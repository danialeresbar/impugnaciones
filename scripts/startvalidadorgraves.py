import os
import sys
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from django.db import connection


# ---------CREACION DE UIDS----------
def get_diffs():
    votacionbulk = []
    cursor = connection.cursor()
    cursor.execute("update estructura_jrv set para_reclamar=true, para_reclamar7=true, para_reclamar8=true, para_reclamar9=true where incidencia_grave = true;")

get_diffs()
