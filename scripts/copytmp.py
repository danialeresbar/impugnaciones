
import sys, os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()

#----------------------------------------------------------------------------
#                  CARGA DE VOTOS A ESCRUTINIO1  no carga partidos

#-----------------------------------------------------------------------------

class Iniciarproceso:
        newfile = open('basicos/2upload.csv', 'w')
        file = open('basicos/3v.csv', mode='r', encoding='ansi')
        lines = file.readlines()
        file.close()
        for line in lines:
                columna = line.split('|')
                if (columna[0] != "codprovincia"):
                        uidcod = "{:02d}".format(int(columna[0])) + "{:03d}".format(int(columna[2])) + "{:04d}".format(int(columna[3])) +\
                                 "{:02d}".format(int(columna[4])) + "{:03d}".format(int(columna[5])) + columna[6] +\
                                 "{:02d}".format(int(columna[7])) + "{:03d}".format(int(columna[13]))
                        newline = uidcod + "," + columna[15] +"\n"
                        newfile.write(newline)
                else:
                        newline = "uid,votos\n"
                        newfile.write(newline)
        newfile.close()
        print("Carga  completa")

