import sys, os, django


os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

#----------------------------------------------------------------------------
#                  CARGA DE ARCHIVOS BASICOS CNE
#-----------------------------------------------------------------------------

from estructura.models import  Provincia, Circunscripcion, Canton, Parroquia,  Zona , Recinto, dignidad, partido, JRV



class upload_ProvinciasCNE():
    file = open('basicos/CNE/PROVINCIA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')

        if (columna[0] != "COD_PROVINCIA"):

            q = Provincia(codprovincia=columna[0], nomprovincia=columna[1])
            q.save()
    print("Carga de provincias completa")

class upload_Circunscripciones():
    file = open('basicos/CNE/CIRCUNSCRIPCION.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_CIRCUNSCRIPCION"):
            Provinciaid = Provincia.objects.get(codprovincia=columna[2])
            q = Circunscripcion(codcircunscripcion=columna[0], nomcircunscripcion=columna[1], provincia=Provinciaid)
            q.save()
    print("Carga de Circusncripciones completa")


class upload_Cantones():
    file = open('basicos/CNE/CANTON.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_CANTON"):
            Provinciaid = Provincia.objects.get(codprovincia=columna[2])
            if (columna[3][0:1] != "0"):
                print(line)
                Circunscripcionid = Circunscripcion.objects.get(codcircunscripcion=columna[3], provincia = Provinciaid)
                q = Canton(codcanton=columna[0], nomcanton=columna[1], provincia=Provinciaid, circunscripcion=Circunscripcionid)
                q.save()
            else:
                q = Canton(codcanton=columna[0], nomcanton=columna[1], provincia=Provinciaid)
                q.save()


    print("Carga de cantones completa")


class upload_Parroquias():
    file = open('basicos/CNE/PARROQUIA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_PARROQUIA"):
            Cantonid = Canton.objects.get(codcanton=columna[2])
            if (columna[3][0:1] != "0"):
                Circunscripcionid = Circunscripcion.objects.get(codcircunscripcion=columna[3], provincia=Cantonid.provincia)
                q = Parroquia(codparroquia=columna[0], nomparroquia=columna[1],canton=Cantonid, circunscripcion=Circunscripcionid)
                q.save()
            else:
                q = Parroquia(codparroquia=columna[0], nomparroquia=columna[1],canton=Cantonid)
                q.save()

    print("Carga de parroquias completa")


class upload_Zonas():
    file = open('basicos/CNE/ZONA.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_ZONA"):
                Parroquiaid = Parroquia.objects.get(codparroquia=columna[2])
                q = Zona(codzona=columna[0],   nomzona=columna[1
                ], parroquia=Parroquiaid,circunscripcion=Parroquiaid.circunscripcion)
                q.save()
    print("Carga de zonas completa")



class upload_Recintos():

    file = open('basicos/CNE/RECINTO.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_PROVINCIA"):
            Parroquiaid = Parroquia.objects.get(codparroquia=columna[6])
            if (columna[9] != "0"):
                Zonaid = Zona.objects.get(parroquia_id=Parroquiaid.pk, codzona=columna[9])
                q = Recinto(codrecinto=columna[11], nomrecinto=columna[12], parroquia=Parroquiaid, zona=Zonaid)
                q.save()
            else:
                q = Recinto(codrecinto=columna[11], nomrecinto=columna[12], parroquia=Parroquiaid)
                q.save()
    print("Carga de recintos completa")



class upload_Dignidades():

    file = open('basicos/CNE/DIGNIDAD.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_DIGNIDAD"):
            print(columna[0])
            q = dignidad(coddignidad=columna[0], nomdignidad=columna[1] )
            q.save()
    print("Carga de dignidades completa")


class upload_Partidos():

    file = open('basicos/CNE/PARTIDOS7.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_DIGNIDAD"):
            Provinciaid = Provincia.objects.get(codprovincia=columna[2])
            print(columna[7])
            Dignidadid = dignidad.objects.get(coddignidad=columna[0])
            q = partido(codpartido=columna[4], nompartido=columna[7], provincia=Provinciaid, dignidad=Dignidadid )
            q.save()
    print("Carga de partidos completa")



class upload_JRVs():
    file = open('basicos/CNE/JRV.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        if (columna[0] != "COD_PROVINCIA"):
            Cantonid = Canton.objects.get(codcanton=columna[4])
            Recintoid = Recinto.objects.get(codrecinto=columna[11])
            jrvnum = columna[13] + columna[14]
            codid= "{:02d}".format(int(columna[0])) + "{:03d}".format(int(columna[4])) + "{:04d}".format(int(columna[6])) + "{:02d}".format(int(columna[9])) + "{:03d}".format(int(columna[13])) + columna[14]
            q = JRV( provincia = Cantonid.provincia,circunscripcion = Cantonid.circunscripcion,canton = Cantonid,parroquia = Recintoid.parroquia,
                zona = Recintoid.zona,recinto = Recintoid,cod = codid, numero = columna[13], genero = columna[14], num_electores = columna[15], observaciones = "", telefonos = "")
            q.save()

    print("Carga de JRVS completa")
