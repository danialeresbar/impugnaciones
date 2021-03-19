import os
import sys
from time import time
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from estructura.models import Provincia, Circunscripcion, Canton, Parroquia, Zona, Recinto, dignidad, partido, JRV


# ---------CARGA DE ARCHIVOS BASICOS CNE----------
def upload_cne_provinces():
    with open('scripts/basicos/CNE/PROVINCIA.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_PROVINCIA":
                Provincia.objects.create(codprovincia=data[0], nomprovincia=data[1])
        print(f'{len(lines) - 1} Provinces has been loaded successfully!')


def upload_circumscriptions():
    with open('scripts/basicos/CNE/CIRCUNSCRIPCION.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_CIRCUNSCRIPCION":
                province = Provincia.objects.get(codprovincia=data[2])
                Circunscripcion.objects.create(
                    codcircunscripcion=data[0],
                    nomcircunscripcion=data[1],
                    provincia=province
                )
        print(f'{len(lines) - 1} Circumscriptions has been loaded successfully!')


def upload_cantons():
    with open('scripts/basicos/CNE/CANTON.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_CANTON":
                province = Provincia.objects.get(codprovincia=data[2])
                if data[3][0:1] != "0":
                    circumscription = Circunscripcion.objects.get(codcircunscripcion=data[3], provincia=province)
                    q = Canton(
                        codcanton=data[0],
                        nomcanton=data[1],
                        provincia=province,
                        circunscripcion=circumscription
                    )
                    q.save()
                else:
                    q = Canton(codcanton=data[0], nomcanton=data[1], provincia=province)
                    q.save()
        print(f'{len(lines) - 1} Cantons has been loaded successfully!')


def upload_parishes():
    with open('scripts/basicos/CNE/PARROQUIA.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_PARROQUIA":
                canton = Canton.objects.get(codcanton=data[2])
                if data[3][0:1] != "0":
                    circumscription = Circunscripcion.objects.get(
                        codcircunscripcion=data[3],
                        provincia=canton.provincia
                    )
                    q = Parroquia(
                        codparroquia=data[0],
                        nomparroquia=data[1],
                        canton=canton,
                        circunscripcion=circumscription
                    )
                    q.save()
                else:
                    q = Parroquia(codparroquia=data[0], nomparroquia=data[1], canton=canton)
                    q.save()
        print(f'{len(lines) - 1} Parishes has been loaded successfully!')


def upload_zones():
    with open('scripts/basicos/CNE/ZONA.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_ZONA":
                parish = Parroquia.objects.get(codparroquia=data[2])
                q = Zona(
                    codzona=data[0],
                    nomzona=data[1],
                    parroquia=parish,
                    circunscripcion=parish.circunscripcion
                )
                q.save()
        print(f'{len(lines) - 1} Zones has been loaded successfully!')


def upload_areas():
    with open('scripts/basicos/CNE/RECINTO.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
    for line in lines:
        data = line.split(';')
        if data[0] != "COD_PROVINCIA":
            parish = Parroquia.objects.get(codparroquia=data[6])
            if data[9] != "0":
                zone = Zona.objects.get(parroquia_id=parish.pk, codzona=data[9])
                q = Recinto(codrecinto=data[11], nomrecinto=data[12], parroquia=parish, zona=zone)
                q.save()
            else:
                q = Recinto(codrecinto=data[11], nomrecinto=data[12], parroquia=parish)
                q.save()
    print(f'{len(lines) - 1} Areas has been loaded successfully!')


def upload_dignities():
    with open('scripts/basicos/CNE/DIGNIDAD.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_DIGNIDAD":
                dignidad.objects.create(
                    coddignidad=data[0],
                    nomdignidad=data[1]
                )
        print(f'{len(lines) - 1} Dignities has been loaded successfully!')


def upload_parties():
    with open('scripts/basicos/CNE/PARTIDOS7.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_DIGNIDAD":
                province = Provincia.objects.get(codprovincia=data[2])
                dignity = dignidad.objects.get(coddignidad=data[0])
                partido.objects.create(
                    codpartido=data[4],
                    nompartido=data[7],
                    provincia=province,
                    dignidad=dignity
                )
        print(f'{len(lines) - 1} Parties has been loaded successfully!')


def upload_jrvs():
    with open('scripts/basicos/CNE/JRV.csv', mode='r', encoding='cp1252') as source:
        lines = source.readlines()
        for line in lines:
            data = line.split(';')
            if data[0] != "COD_PROVINCIA":
                canton = Canton.objects.get(codcanton=data[4])
                area = Recinto.objects.get(codrecinto=data[11])
                jrvnum = data[13] + data[14]
                codid = "{:02d}".format(int(data[0])) + "{:03d}".format(int(data[4])) + "{:04d}".format(int(data[6])) +\
                        "{:02d}".format(int(data[9])) + "{:03d}".format(int(data[13])) + data[14]
                q = JRV(
                    provincia=canton.provincia,
                    circunscripcion=canton.circunscripcion,
                    canton=canton,
                    parroquia=area.parroquia,
                    zona=area.zona,
                    recinto=area,
                    cod=codid,
                    numero=data[13],
                    genero=data[14],
                    num_electores=data[15],
                    observaciones="",
                    telefonos=""
                )
                q.save()
        print(f'{len(lines) - 1} JRVs has been loaded successfully!')


start_time = time()
upload_cne_provinces()
upload_circumscriptions()
upload_cantons()
upload_parishes()
upload_zones()
upload_areas()
upload_dignities()
upload_parties()
upload_jrvs()
elapsed_time = time() - start_time
print(f'Elapsed time: {elapsed_time} seconds')
