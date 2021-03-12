from django.core.management.base import BaseCommand, CommandError
from tmp.models import escrutinio1
from comparacion.models import votacion
from django.db import connection
import requests


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Convertir CSV a formato unico MMV
        newfile = open('basicos/2uploadpres.csv', 'w')
        newfile.write("uid,cod_junta,sufragantes,nulos,blancos,votos\n")
        response1 = requests.get("https://impugnaciones.andresarauz.ec/resultados/resultados_1.csv").text.split("\n")
        response7 = requests.get("https://impugnaciones.andresarauz.ec/resultados/resultados_7.csv").text.split("\n")
        response8 = requests.get("https://impugnaciones.andresarauz.ec/resultados/resultados_8.csv").text.split("\n")
        response9 = requests.get("https://impugnaciones.andresarauz.ec/resultados/resultados_9.csv").text.split("\n")
        lines=response1+response7+response8+response9

        for line in lines:
            columna = line.split('|')

            try:
                uidcod = "{:02d}".format(int(columna[1])) + "{:03d}".format(int(columna[2])) + \
                         "{:04d}".format(int(columna[4])) + "{:02d}".format(int(columna[5])) + \
                         "{:03d}".format(int(columna[6])) + columna[7] + \
                         "{:02d}".format(int(columna[0])) + "{:04d}".format(int(columna[10]))
                newline = uidcod + "," + columna[8] + "," + columna[11] + "," + columna[12] + "," + columna[13] + "," + \
                          columna[14]+"\n"
                newfile.write(newline)
            except:
                print(line)

        newfile.close()
        print("base de datos convertida a formato MMV")

        # copiar CSV a BASE DE DATOS TEMPORAL
        cursor = connection.cursor()
        cursor.execute("TRUNCATE tmp_escrutinio1")
        insert_count = escrutinio1.objects.from_csv('basicos/2uploadpres.csv', delimiter=",")
        print("{} records cargados en la BD temporal".format(insert_count))
        # Cargar datos de bd temporal a columna correspondiente
        cursor.execute("UPDATE comparacion_votacion v SET cne1 = e.votos, acta = e.cod_junta, sufragantes=e.sufragantes, nulos=e.nulos, blancos=e.blancos   FROM tmp_escrutinio1 e WHERE v.cod = e.uid")
        print("Columna de escrutinio actualizada")

        cursor.execute(
            "update comparacion_votacion set diff1 = cne1 - delegados  where delegados is not null and cne1 - delegados <> 0 ")
        cursor.execute(
            "update comparacion_votacion set diff2 = cne1 - app_digitacion  where app_digitacion is not null and cne1 - app_digitacion <> 0 ")
        newfile = open('basicos/diferencias.csv', 'w')
        uidJRVDigpartidos = votacion.objects.raw(
            'select * from comparacion_votacion where diff1 is not null or diff2 is not null')

        for uid in uidJRVDigpartidos:
            if uid.zona is None:
                zona = "0"
            else:
                zona = str(uid.zona.codzona)

            line = str(uid.provincia.codprovincia) + "," + str(uid.canton.codcanton) + "," + str(
                uid.parroquia.codparroquia) + "," + zona + "," + \
                   str(uid.recinto.codrecinto) + "," + str(uid.jrv.numero) + "," + uid.jrv.genero + "," + str(
                uid.dignidad.coddignidad) + "," + str(uid.partido.codpartido) + "," + str(uid.cne1) + "," + str(
                uid.diff1) + "," + str(uid.diff2) + "\n"
            newfile.write(line)
        newfile.close()
        print("diferencias generadas")
