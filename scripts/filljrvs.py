import datetime
import os
import requests
import sys
import django

from django.utils.timezone import get_current_timezone


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from estructura.models import JRV


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/presidente_cne", headers=headers)
votos = response.json()
votacionbulk = []
for voto in votos:
    datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
            "{:03d}".format(int(voto['numero'])) + voto['genero']
    votos = voto['votos']
    error = ['error']
    if voto['idpartido'] == '510':
        imagen = voto['idimagen']
        if imagen is None:
            imagen = ""
        if imagen != "":
            imagen = "https://imagenes.andresarauz.ec/images/"+imagen
            votacionbulk.append(JRV(cod=codne, acta_delegados=imagen))
JRV.objects.bulk_update(votacionbulk, ['acta_delegados'])
votacionbulk.clear()


# ASAMBLEA NACIONAL
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/nacional_cne", headers=headers)
votos = response.json()

for voto in votos:
    idpartido = voto['idpartido_cne']
    if idpartido is not None:
        datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
        codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
                "{:03d}".format(int(voto['numero'])) + voto['genero']
        votos = voto['votos']
        error = ['error']
        imagen = voto['idimagen']
        if imagen is None:
            imagen = ""
        if imagen != "":
            imagen = "https://imagenes.andresarauz.ec/images/"+imagen
            votacionbulk.append(JRV(cod=codne, acta_delegadosnal=imagen))

JRV.objects.bulk_update(votacionbulk, ['acta_delegadosnal'])
votacionbulk.clear()


# ASAMBLEA PROVINCIAL
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/provincial_cne", headers=headers)
votos = response.json()

for voto in votos:
    idpartido = voto['idpartido_cne']
    if idpartido is not None:
        datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
        codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
                "{:03d}".format(int(voto['numero'])) + voto['genero']
        votos = voto['votos']
        error = ['error']
        imagen = voto['idimagen']
        if imagen is None:
            imagen = ""
        if imagen != "":
            imagen = "https://imagenes.andresarauz.ec/images/"+imagen
            votacionbulk.append(JRV(cod=codne, acta_delegadosprov=imagen))

JRV.objects.bulk_update(votacionbulk, ['acta_delegadosprov'])
votacionbulk.clear()


# PARLAMENTO ANDINO
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/andino_cne", headers=headers)
votos = response.json()

for voto in votos:
    idpartido = voto['idpartido_cne']
    if idpartido is not None:
        datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
        codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
                "{:03d}".format(int(voto['numero'])) + voto['genero']
        votos = voto['votos']
        error = ['error']
        imagen = voto['idimagen']
        if imagen is None:
            imagen = ""
        if imagen != "":
            imagen = "https://imagenes.andresarauz.ec/images/"+imagen
            votacionbulk.append(JRV(cod=codne, acta_delegadosand=imagen))

JRV.objects.bulk_update(votacionbulk, ['acta_delegadosand'])
votacionbulk.clear()
