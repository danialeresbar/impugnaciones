import sys, os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from comparacion.models import  votacion
from estructura.models import JRV
from django.db import connection

#----------------------------------------------------------------------------
#                  CREACION DE UIDS

#-----------------------------------------------------------------------------

class get_Diffs:
    votacionbulk = []
    cursor = connection.cursor()
    cursor.execute("update estructura_jrv set para_reclamar=true, para_reclamar7=true, para_reclamar8=true, para_reclamar9=true where incidencia_grave = true;")
