from django.core.management.base import BaseCommand, CommandError
from tmp.models import escrutinio1, delegados
from django.db import connection
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("TRUNCATE tmp_delegados")
        insert_count = delegados.objects.from_csv('basicos/4upload.csv', delimiter=",")
        print("{} records cargados en la BD temporal".format(insert_count))
        # Cargar datos de bd temporal a columna correspondiente
        cursor.execute("UPDATE comparacion_votacion v SET delegados = e.votos FROM tmp_delegados e WHERE v.cod = e.uid")
        print("Columna de escrutinio actualizada")
