import os
import sys
import django


sys.path.append('/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'impugnaciones.settings'
django.setup()


from django.core.paginator import Paginator
from comparacion.models import votacion


vot = votacion.objects.filter(dignidad=1, canton=260)
print(len(vot))
paginator = Paginator(vot, 10)
page = paginator.get_page(1)
print(page)
