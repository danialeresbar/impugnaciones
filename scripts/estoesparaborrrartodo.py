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
    cursor = connection.cursor()
    #PRESIDENTE
    cursor.execute("update estructura_jrv set observaciones = '';")
    cursor.execute("update estructura_jrv set incidencia = false;")
    cursor.execute("update estructura_jrv set telefonos = '';")
    cursor.execute("update estructura_jrv set tmpdiff1=null, tmpdiff2=null,para_validar=false, para_validar7=false, para_validar8=false, para_validar9=false, maxdiff = null,maxdiffnal = null, maxdiffprov = null, maxdiffand = null;")
    cursor.execute("update estructura_jrv set appsufragantes=null, appblancos=null,appnulos=null, digitasufragantes=null, digitablancos=null, digitanulos=null, cnesufragantes = null,cneblancos = null, cnenulos = null;")
    cursor.execute("update estructura_jrv set quitaron=null, pusieron=null,quitaron7=null, pusieron7=null,quitaron8=null,       pusieron8=null,quitaron9=null, pusieron9=null")
    cursor.execute("update estructura_jrv set difnum1=False, difnum7=False,difnum8=False, difnum9=False,otro1=null, otro7=null,otro8=null, otro9=null")
    cursor.execute("update estructura_jrv set no_procede=False, para_reclamar=False, no_procede7=False, para_reclamar7=False,no_procede8=False, para_reclamar8=False,no_procede9=False, para_reclamar9=False")
    cursor.execute("update comparacion_votacion set delegados = null ")
    cursor.execute("update comparacion_votacion set cne1=null ")
    cursor.execute("update comparacion_votacion set acta=null, sufragantes=null, blancos=null , nulos=null")
    cursor.execute("update comparacion_votacion set diff1=null, diff2=null")