import datetime
import os
import django
import requests
import sys
from django.utils.timezone import get_current_timezone


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from comparacion.models import votacion


# PRESIDENTE Y VICEPRESIDENTE
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/presidente_cne", headers=headers)
votos = response.json()

votacionbulk = []
for voto in votos:
    datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
    if voto['idpartido_cne'] is not None:
        codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
            "{:03d}".format(int(voto['numero'])) + voto['genero'] + "01" + \
            "{:04d}".format(int(voto['idpartido_cne']))
        votos = voto['votos']
        print(voto['idpartido_cne'])
        votacionbulk.append(votacion(cod=codne, delegados=votos))
votacion.objects.bulk_update(votacionbulk, ['delegados'])
votacionbulk.clear()
print("presidente ok")

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/nacional_cne", headers=headers)
votos = response.json()

for voto in votos:
    datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
            "{:03d}".format(int(voto['numero'])) + voto['genero'] + "09" + "{:04d}".format(int(voto['idpartido_cne']))
    votos = voto['votos']
    votacionbulk.append(votacion(cod=codne, delegados=votos))
votacion.objects.bulk_update(votacionbulk, ['delegados'])
votacionbulk.clear()
print("asamblea nacional ok")


# ASAMBLEA PROVINCIAL
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/provincial_cne", headers=headers)
votos = response.json()

for voto in votos:
    idpartido = voto['idpartido_cne']
    if idpartido is not None:
        datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
        codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
                "{:03d}".format(int(voto['numero'])) + voto['genero'] + "07" + "{:04d}".format(int(voto['idpartido_cne']))
        votos = voto['votos']
        votacionbulk.append(votacion(cod=codne, delegados=votos))
votacion.objects.bulk_update(votacionbulk, ['delegados'])
votacionbulk.clear()
print("provinciales ok")


#PARLAMENTO ANDINO
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
response = requests.get("https://controlelectoral.unionporlaesperanza.com/api/andino_cne", headers=headers)
votos = response.json()

for voto in votos:
    datetime_time = datetime.datetime.fromtimestamp(voto['fecha'], tz=get_current_timezone())
    codne = "{:02d}".format(int(voto['idprovincia_cne'])) + "{:03d}".format(int(voto['idcanton_cne'])) + "{:04d}".format(int(voto['idparroquia_cne'])) + "{:02d}".format(int(voto['idzona_cne'])) +\
            "{:03d}".format(int(voto['numero'])) + voto['genero'] + "08" + "{:04d}".format(int(voto['idpartido_cne']))
    votos = voto['votos']
    votacionbulk.append(votacion(cod=codne, delegados=votos))
votacion.objects.bulk_update(votacionbulk, ['delegados'])
votacionbulk.clear()
print("parlamento ok")
