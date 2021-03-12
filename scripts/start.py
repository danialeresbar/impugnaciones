import os
import sys
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from estructura.models import Provincia, Circunscripcion, Canton, Parroquia, Zona, Recinto, dignidad, partido, JRV


# ---------CARGA DE ARCHIVOS BASICOS CNE----------
def upload_cne_provincias():
    file = open('basicos/CNE/PROVINCIA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_PROVINCIA":
            q = Provincia(codprovincia=columna[0], nomprovincia=columna[1])
            q.save()
    print("Carga de provincias completa")


def upload_circunscripciones():
    file = open('basicos/CNE/CIRCUNSCRIPCION.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_CIRCUNSCRIPCION":
            provincia_id = Provincia.objects.get(codprovincia=columna[2])
            q = Circunscripcion(codcircunscripcion=columna[0], nomcircunscripcion=columna[1], provincia=provincia_id)
            q.save()
    print("Carga de Circusncripciones completa")


def upload_cantones():
    file = open('basicos/CNE/CANTON.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_CANTON":
            provincia_id = Provincia.objects.get(codprovincia=columna[2])
            if columna[3][0:1] != "0":
                print(line)
                circunscripcion_id = Circunscripcion.objects.get(codcircunscripcion=columna[3], provincia=provincia_id)
                q = Canton(
                    codcanton=columna[0],
                    nomcanton=columna[1],
                    provincia=provincia_id,
                    circunscripcion=circunscripcion_id
                )
                q.save()
            else:
                q = Canton(codcanton=columna[0], nomcanton=columna[1], provincia=provincia_id)
                q.save()
    print("Carga de cantones completa")


def upload_parroquias():
    file = open('basicos/CNE/PARROQUIA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_PARROQUIA":
            canton_id = Canton.objects.get(codcanton=columna[2])
            if columna[3][0:1] != "0":
                circunscripcion_id = Circunscripcion.objects.get(
                    codcircunscripcion=columna[3],
                    provincia=canton_id.provincia
                )
                q = Parroquia(
                    codparroquia=columna[0],
                    nomparroquia=columna[1],
                    canton=canton_id,
                    circunscripcion=circunscripcion_id
                )
                q.save()
            else:
                q = Parroquia(codparroquia=columna[0], nomparroquia=columna[1], canton=canton_id)
                q.save()
    print("Carga de parroquias completa")


def upload_zonas():
    file = open('basicos/CNE/ZONA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_ZONA":
            parroquia_id = Parroquia.objects.get(codparroquia=columna[2])
            q = Zona(
                codzona=columna[0],
                nomzona=columna[1],
                parroquia=parroquia_id,
                circunscripcion=parroquia_id.circunscripcion
            )
            q.save()
    print("Carga de zonas completa")


def upload_recintos():
    file = open('basicos/CNE/RECINTO.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_PROVINCIA":
            parroquia_id = Parroquia.objects.get(codparroquia=columna[6])
            if columna[9] != "0":
                zona_id = Zona.objects.get(parroquia_id=parroquia_id.pk, codzona=columna[9])
                q = Recinto(codrecinto=columna[11], nomrecinto=columna[12], parroquia=parroquia_id, zona=zona_id)
                q.save()
            else:
                q = Recinto(codrecinto=columna[11], nomrecinto=columna[12], parroquia=parroquia_id)
                q.save()
    print("Carga de recintos completa")


def upload_dignidades():
    file = open('basicos/CNE/DIGNIDAD.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_DIGNIDAD":
            print(columna[0])
            q = dignidad(coddignidad=columna[0], nomdignidad=columna[1])
            q.save()
    print("Carga de dignidades completa")


def upload_partidos():
    file = open('basicos/CNE/PARTIDOS7.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_DIGNIDAD":
            provincia_id = Provincia.objects.get(codprovincia=columna[2])
            print(columna[7])
            dignidad_id = dignidad.objects.get(coddignidad=columna[0])
            q = partido(codpartido=columna[4], nompartido=columna[7], provincia=provincia_id, dignidad=dignidad_id)
            q.save()
    print("Carga de partidos completa")


def upload_jrvs():
    file = open('basicos/CNE/JRV.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if columna[0] != "COD_PROVINCIA":
            canton_id = Canton.objects.get(codcanton=columna[4])
            recinto_id = Recinto.objects.get(codrecinto=columna[11])
            jrvnum = columna[13] + columna[14]
            codid = "{:02d}".format(int(columna[0])) + "{:03d}".format(int(columna[4])) + "{:04d}".format(int(columna[6])) + "{:02d}".format(int(columna[9])) + "{:03d}".format(int(columna[13])) + columna[14]
            q = JRV(
                provincia=canton_id.provincia,
                circunscripcion=canton_id.circunscripcion,
                canton=canton_id,
                parroquia=recinto_id.parroquia,
                zona=recinto_id.zona,
                recinto=recinto_id,
                cod=codid,
                numero=columna[13],
                genero=columna[14],
                num_electores=columna[15],
                observaciones="",
                telefonos=""
            )
            q.save()
    print("Carga de JRVS completa")


upload_cne_provincias()
upload_circunscripciones()
upload_cantones()
upload_parroquias()
upload_zonas()
upload_recintos()
upload_dignidades()
upload_partidos()
upload_jrvs()
