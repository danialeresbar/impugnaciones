import datetime
import os
import sys
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from rolepermissions.roles import assign_role
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_users():
    # g = Group.objects.get(name='Abogados')
    file = open('basicos/abogados.csv', mode='r', encoding='cp1252')
    lines = file.readlines()
    file.close()
    for line in lines:
        columna = line.split(';')
        q = User()
        q.set_password(columna[1])
        q.last_login = datetime.datetime.now()
        q.is_superuser = "0"
        q.username = columna[2]
        q.first_name = columna[3]
        q.email = columna[4]
        q.is_staff = "1"
        q.is_active = "1"
        q.date_joined = datetime.datetime.now()
        q.last_name = columna[5]
        try:
            q.save()
            rolo = columna[6]
            print(rolo)
            assign_role(q, rolo)
            print(q.email)
        except Exception as e:
            print(f'El usuario ya ha sido registrado: \n{e}')
        # g.user_set.add(q)


upload_users()
