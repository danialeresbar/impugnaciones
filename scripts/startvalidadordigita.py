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


    #PRESIDENTE
    cursor.execute("update estructura_jrv set tmpdiff1=null, tmpdiff2=null")
    uidDiff1s = votacion.objects.raw( "select t.cod, min(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 < 0 and v.dignidad_id=1 and p.codpartido = 1030 group by t.cod ")
    for uid1 in uidDiff1s:
        votacionbulk.append(JRV(cod=uid1.cod, tmpdiff1 =uid1.min))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff1'])
    votacionbulk.clear()
    print("presidente1 validado")

    uidDiff2s = votacion.objects.raw(
        "select t.cod, max(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 > 0 and v.dignidad_id=1 and p.codpartido != 1030 group by t.cod ")
    for uid2 in uidDiff2s:
        votacionbulk.append(JRV(cod=uid2.cod, tmpdiff2=uid2.max))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff2'])
    votacionbulk.clear()
    cursor.execute("update estructura_jrv set maxdiff = GREATEST(abs(tmpdiff1), tmpdiff2);"
                   "update estructura_jrv set maxdiff = null where tmpdiff1 is null; "
                   "update estructura_jrv set maxdiff = null where tmpdiff2 is null; "
                   "update estructura_jrv set para_validar = True where maxdiff is not null;"
                   "update estructura_jrv set tmpdiff1=null, tmpdiff2=null;")
    print("presidente2 validado")

 #ASAMBLEA NACIONAL
    uidDiff1s = votacion.objects.raw( "select t.cod, min(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 < 0 and v.dignidad_id=9 and p.codpartido = 1030 group by t.cod ")
    for uid1 in uidDiff1s:
        votacionbulk.append(JRV(cod=uid1.cod, tmpdiff1 =uid1.min))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff1'])
    votacionbulk.clear()

    uidDiff2s = votacion.objects.raw(
        "select t.cod, max(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 > 0 and v.dignidad_id=9 and p.codpartido != 1030 group by t.cod ")
    for uid2 in uidDiff2s:
        votacionbulk.append(JRV(cod=uid2.cod, tmpdiff2=uid2.max))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff2'])
    votacionbulk.clear()
    cursor.execute("update estructura_jrv set maxdiffnal = GREATEST(abs(tmpdiff1), tmpdiff2); "
                   "update estructura_jrv set maxdiffnal = null where tmpdiff1 is null; "
                   "update estructura_jrv set maxdiffnal = null where tmpdiff2 is null; "
                   "update estructura_jrv set para_validar9 = True where maxdiffnal is not null;"
                   "update estructura_jrv set tmpdiff1=null, tmpdiff2=null;")
    print("asamblea validado")

 #ASAMBLEA PROVINCIAL
    cursor.execute("update estructura_jrv set tmpdiff1=null, tmpdiff2=null")
    uidDiff1s = votacion.objects.raw( "select t.cod, min(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 < 0 and v.dignidad_id=7 and p.codpartido = 1030 group by t.cod ")
    for uid1 in uidDiff1s:
        votacionbulk.append(JRV(cod=uid1.cod, tmpdiff1 =uid1.min))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff1'])
    votacionbulk.clear()

    uidDiff2s = votacion.objects.raw(
        "select t.cod, max(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 > 0 and v.dignidad_id=7 and p.codpartido != 1030 group by t.cod ")
    for uid2 in uidDiff2s:
        votacionbulk.append(JRV(cod=uid2.cod, tmpdiff2=uid2.max))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff2'])
    votacionbulk.clear()
    cursor.execute("update estructura_jrv set maxdiffprov = GREATEST(abs(tmpdiff1), tmpdiff2);"
                   "update estructura_jrv set maxdiffprov = null where tmpdiff1 is null; "
                   "update estructura_jrv set maxdiffprov = null where tmpdiff2 is null; "
                   "update estructura_jrv set para_validar7 = True where maxdiffprov is not null;"
                   "update estructura_jrv set tmpdiff1=null, tmpdiff2=null;")
    print("provinicial validado")

 #PARLAMENTO
    uidDiff1s = votacion.objects.raw( "select t.cod, min(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 < 0 and v.dignidad_id=8 and p.codpartido = 1030 group by t.cod ")
    for uid1 in uidDiff1s:
        votacionbulk.append(JRV(cod=uid1.cod, tmpdiff1 =uid1.min))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff1'])
    votacionbulk.clear()

    uidDiff2s = votacion.objects.raw(
        "select t.cod, max(v.diff2) from estructura_jrv as t join comparacion_votacion as v on  t.cod = v.jrv_id join estructura_partido as p on v.partido_id = p.id where v.diff2 is not null and v.diff2 > 0 and v.dignidad_id=8 and p.codpartido != 1030 group by t.cod ")
    for uid2 in uidDiff2s:
        votacionbulk.append(JRV(cod=uid2.cod, tmpdiff2=uid2.max))
    JRV.objects.bulk_update(votacionbulk, ['tmpdiff2'])
    votacionbulk.clear()
    cursor.execute("update estructura_jrv set maxdiffand = GREATEST(abs(tmpdiff1), tmpdiff2);"
                   "update estructura_jrv set maxdiffand = null where tmpdiff1 is null; "
                   "update estructura_jrv set maxdiffand = null where tmpdiff2 is null; "
                   "update estructura_jrv set para_validar8 = True where maxdiffand is not null;"
                   "update estructura_jrv set tmpdiff1=null, tmpdiff2=null;")
    print("andino validado")