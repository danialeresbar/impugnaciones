import sys, os, django
import requests
import datetime
from django.utils.timezone import get_current_timezone
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

from comparacion.models import votacion
from estructura.models import JRV

#IMAGENES PRESIDENTE
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://adhesiones.unionporlaesperanza.com/api/presidente_cne", headers=headers)
votos = response.json()
total=0
count = 0
oldcne = "1"
votacionbulk = []
votacionbulk2 = []
votacionbulk3 = []
for voto in votos:

    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(
        int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(
        int(voto['idzona_cne'])) + "{:03d}".format(int(voto['numero'])) + voto['genero']

    if voto['idpartido_cne'] is None :
        imagen=voto['idimagen']
        if imagen is not None:
            if imagen != "":
                if codne == oldcne: count= count+1
                else: count=1
                oldcne = codne
                imagen="https://imagenes.andresarauz.ec/images/"+imagen
                if count == 1: votacionbulk.append(JRV(cod=codne, acta_delegados=imagen))
                if count == 2: votacionbulk2.append(JRV(cod=codne, acta_delegados2=imagen))
                if count == 3: votacionbulk3.append(JRV(cod=codne, acta_delegados3=imagen))
                print(codne+ " -- " + str(count))

JRV.objects.bulk_update(votacionbulk, ['acta_delegados'])
JRV.objects.bulk_update(votacionbulk2, ['acta_delegados2'])
JRV.objects.bulk_update(votacionbulk3, ['acta_delegados3'])
votacionbulk.clear()
votacionbulk2.clear()
votacionbulk3.clear()

# IMAGENES ASAMBLEA
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/nacional_cne", headers=headers)
votos = response.json()
total = 0
count = 0
oldcne = "1"
votacionbulk = []
votacionbulk2 = []
votacionbulk3 = []
for voto in votos:

    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(
        int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(
        int(voto['idzona_cne'])) + "{:03d}".format(int(voto['numero'])) + voto['genero']

    if voto['idpartido_cne'] is None:
        imagen = voto['idimagen']
        if imagen is not None:
            if imagen != "":
                if codne == oldcne:
                    count = count + 1
                else:
                    count = 1
                oldcne = codne
                imagen = "https://imagenes.andresarauz.ec/images/" + imagen
                if count == 1: votacionbulk.append(JRV(cod=codne, acta_delegadosnal=imagen))
                if count == 2: votacionbulk2.append(JRV(cod=codne, acta_delegadosnal2=imagen))
                if count == 3: votacionbulk3.append(JRV(cod=codne, acta_delegadosnal3=imagen))
                print(codne + " -- " + str(count))

JRV.objects.bulk_update(votacionbulk, ['acta_delegadosnal'])
JRV.objects.bulk_update(votacionbulk2, ['acta_delegadosnal2'])
JRV.objects.bulk_update(votacionbulk3, ['acta_delegadosnal3'])
votacionbulk.clear()
votacionbulk2.clear()
votacionbulk3.clear()

# IMAGENES PROVINCIAL
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/provincial_cne", headers=headers)
votos = response.json()
total = 0
count = 0
oldcne = "1"
votacionbulk = []
votacionbulk2 = []
votacionbulk3 = []
for voto in votos:

    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(
        int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(
        int(voto['idzona_cne'])) + "{:03d}".format(int(voto['numero'])) + voto['genero']

    if voto['idpartido_cne'] is None:
        imagen = voto['idimagen']
        if imagen is not None:
            if imagen != "":
                if codne == oldcne:
                    count = count + 1
                else:
                    count = 1
                oldcne = codne
                imagen = "https://imagenes.andresarauz.ec/images/" + imagen
                if count == 1: votacionbulk.append(JRV(cod=codne, acta_delegadosprov=imagen))
                if count == 2: votacionbulk2.append(JRV(cod=codne, acta_delegadosprov2=imagen))
                if count == 3: votacionbulk3.append(JRV(cod=codne, acta_delegadosprov3=imagen))
                print(codne + " -- " + str(count))

JRV.objects.bulk_update(votacionbulk, ['acta_delegados'])
JRV.objects.bulk_update(votacionbulk2, ['acta_delegados2'])
JRV.objects.bulk_update(votacionbulk3, ['acta_delegados3'])
votacionbulk.clear()
votacionbulk2.clear()
votacionbulk3.clear()

# IMAGENES ANDINO
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/andino_cne", headers=headers)
votos = response.json()
total = 0
count = 0
oldcne = "1"
votacionbulk = []
votacionbulk2 = []
votacionbulk3 = []
for voto in votos:

    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(
        int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(
        int(voto['idzona_cne'])) + "{:03d}".format(int(voto['numero'])) + voto['genero']

    if voto['idpartido_cne'] is None:
        imagen = voto['idimagen']
        if imagen is not None:
            if imagen != "":
                if codne == oldcne:
                    count = count + 1
                else:
                    count = 1
                oldcne = codne
                imagen = "https://imagenes.andresarauz.ec/images/" + imagen
                if count == 1: votacionbulk.append(JRV(cod=codne, acta_delegadosand=imagen))
                if count == 2: votacionbulk2.append(JRV(cod=codne, acta_delegadosand2=imagen))
                if count == 3: votacionbulk3.append(JRV(cod=codne, acta_delegadosand3=imagen))
                print(codne + " -- " + str(count))

JRV.objects.bulk_update(votacionbulk, ['acta_delegadosand'])
JRV.objects.bulk_update(votacionbulk2, ['acta_delegadosand2'])
JRV.objects.bulk_update(votacionbulk3, ['acta_delegadosand3'])
votacionbulk.clear()
votacionbulk2.clear()
votacionbulk3.clear()
