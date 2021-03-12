import datetime
import os
import django
import requests
import sys
from django.utils.timezone import get_current_timezone


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from estructura.models import JRV


def start_json_incidences_ext():
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjogImltcHVnbmFjaW9uZXMifQ.G5YNzhFoCisuRQw60cPritxg2hiJy-dgg-QgeXiN2LY"}
    response = requests.get(
        "https://controlelectoral.unionporlaesperanza.com/api/incidencias_combined_cne",
        headers=headers
    )
    incidencias = response.json()

    for incidencia in incidencias:
        datetime_time = datetime.datetime.fromtimestamp(incidencia['fecha'], tz=get_current_timezone())
        codne = "{:02d}".format(int(incidencia['idprovincia_cne'])) + "{:03d}".format(int(incidencia['idcanton_cne'])) + "{:04d}".format(int(incidencia['idparroquia_cne'])) + "{:02d}".format(int(incidencia['idzona_cne']))+"{:03d}".format(int(incidencia['numero'])) + incidencia['genero']
        provincial = str(incidencia['cadena_llamada']['cantonales']).replace("}, {", "\n")[2:-2]
        cantonal = str(incidencia['cadena_llamada']['cantonales']).replace("}, {", "\n")[2:-2]
        parroquial = str(incidencia['cadena_llamada']['parroquiales']).replace("}, {", "\n")[2:-2]
        recinto = str(incidencia['cadena_llamada']['coordinadores_recinto']).replace("}, {", "\n")[2:-2]
        delegado_mesa = str(incidencia['cadena_llamada']['delegado_mesa']).replace("}, {", "\n")[2:-2]
        telefonospiramide = "Delegado de Mesa: \n" + delegado_mesa + "\n--------------------------------------\nCoordinador(es) de Recinto: \n" + recinto + "\n--------------------------------------\nCoordinador(es) Parroquiales: \n" +\
                  parroquial + "\n--------------------------------------\nCoordinador(es) Cantonales: \n" + cantonal + "\n--------------------------------------\nCoordinadores Provinciales: \n" + provincial

        try:
            q = JRV.objects.get(cod=codne)
            q.incidencia = True
            q.fecha_incidencia = datetime_time
            if str(datetime_time) not in q.observaciones:
                q.observaciones = str(datetime_time) + "|" + incidencia['tipo'] + " -->" + \
                                  incidencia['descripcion'] + "\n"
            q.telefonos = telefonospiramide
            q.save()
        except Exception as e:
            print(f'{codne} \n{e}')


start_json_incidences_ext()
