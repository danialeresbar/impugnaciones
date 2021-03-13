from django.core.management.base import BaseCommand
from django.db import connection
from tmp.models import digitacion_nuestra
from comparacion.models import votacion


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Convertir CSV a formato unico MMV
        newfile = open('basicos/presidente_digitadores_cne_10_02_2021', 'w')
        newfile.write("uid,votos\n")

        digfile = open('basicos/provincial_digitadores_cne_10_02_2021v2.csv', 'r')
        lines = digfile.readlines()

        for line in lines:
            columna = line.split(',')
            try:
                uidcod = "{:02d}".format(int(columna[0])) + "{:03d}".format(int(columna[1])) + \
                         "{:04d}".format(int(columna[2])) + "{:02d}".format(int(columna[3])) + \
                         "{:03d}".format(int(columna[6])) + columna[7] + \
                         "07" + "{:04d}".format(int(columna[9]))
                newline = uidcod + "," + columna[10] + "\n"
                newfile.write(newline)
            except Exception as e:
                print(f'Error: \n{e}')

        newfile.close()
        print("base de datos convertida a formato MMV")
        cursor = connection.cursor()
        cursor.execute("TRUNCATE tmp_digitacion_nuestra")
        insert_count = digitacion_nuestra.objects.from_csv('basicos/2uploaddigita.csv', delimiter=";")
        print(f'{insert_count} registros cargados en la BD temporal')
        # Cargar datos de bd temporal a columna correspondiente
        cursor.execute("UPDATE comparacion_votacion v SET app_digitacion = e.votos  FROM tmp_digitacion_nuestra e WHERE v.cod = e.uid")
        print("Columna de Digita actualizada")

        cursor.execute("update comparacion_votacion set diff1 = cne1 - delegados  where delegados is not null and cne1 - delegados <> 0 ")
        cursor.execute("update comparacion_votacion set diff2 = cne1 - app_digitacion  where app_digitacion is not null and cne1 - app_digitacion <> 0 ")
        newfile = open('basicos/diferencias.csv', 'w')
        uidJRVDigpartidos = votacion.objects.raw('select * from comparacion_votacion where diff1 is not null or diff2 is not null')

        for uid in uidJRVDigpartidos:
            if uid.zona is None:
                zona = "0"
            else:
                zona = str(uid.zona.codzona)

            line = str(uid.provincia.codprovincia) + "," + str(uid.canton.codcanton) + "," + \
                   str(uid.parroquia.codparroquia) + "," + zona + "," + str(uid.recinto.codrecinto) + "," + \
                   str(uid.jrv.numero) + "," + uid.jrv.genero + "," + str(uid.dignidad.coddignidad) + "," + \
                   str(uid.partido.codpartido) + "," + str(uid.cne1) + "," + str(uid.diff1) + "," + \
                   str(uid.diff2) + "\n"
            newfile.write(line)
        newfile.close()
        print("diferencias generadas")
