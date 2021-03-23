import xlwt
from dal import autocomplete
from dal_admin_filters import AutocompleteFilter
from requests.utils import requote_uri

from django.contrib.auth.decorators import  login_required
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

# from comparacion.models import votacion
from estructura.models import Parroquia, Zona, Canton, Provincia, partido, JRV
from comparacion import forms


class comp_ParroquiaFilter(AutocompleteFilter):
    title = 'Parroquia'                    # filter's title
    field_name = 'parroquia'           # field name - ForeignKey to Country model
    autocomplete_url = 'cparroquia-autocomplete' # url name of Country autocomplete view


class UProvinciaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #   return models.Parroquia.objects.none()
        qs = Provincia.objects.all()
        print("ok")
        print(self)
        if self.q:
            print(self)
            print(self.q)
            print("pasamos")
            qs = qs.filter(uid__provincia_NOM_PROVINCIA__icontains=self.q)
        return qs


class CParroquiaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #   return models.Parroquia.objects.none()
        qs = Parroquia.objects.all()
        canton = self.forwarded.get('canton', None)
        print(canton)
        if canton:
            qs = qs.filter(canton_id=canton)

        if self.q:
            qs = qs.filter(NOM_PARROQUIA__contains=self.q)

        return qs


class CZonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #   return models.Parroquia.objects.none()
        qs = Zona.objects.all()
        parroquia = self.forwarded.get('parroquia', None)
        print(parroquia)
        if parroquia:
            qs = qs.filter(parroquia_id=parroquia)

        if self.q:
            qs = qs.filter(NOM_ZONA__contains=self.q)

        return qs


class CCantonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #   return models.Parroquia.objects.none()
        qs = Canton.objects.all()
        provincia = self.forwarded.get('provincia', None)
        print(provincia)
        if provincia:
            qs = qs.filter(provincia_id=provincia)

        if self.q:
            qs = qs.filter(NOM_CANTON__contains=self.q)

        return qs

class CProvinciaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #   return models.Parroquia.objects.none()
        qs = Provincia.objects.all()

        if self.q:
            qs = qs.filter(NOM_PROVINCIA__icontains=self.q)

        return qs


# class votacionListView(generic.ListView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class votacionCreateView(generic.CreateView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class votacionDetailView(generic.DetailView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class votacionUpdateView(generic.UpdateView):
#     model = votacion
#     form_class = forms.votacionForm
#     pk_url_kwarg = "pk"
#
#
# class fantasmaListView(generic.ListView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class fantasmaCreateView(generic.CreateView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class fantasmaDetailView(generic.DetailView):
#     model = votacion
#     form_class = forms.votacionForm
#
#
# class fantasmaUpdateView(generic.UpdateView):
#     model = votacion
#     form_class = forms.votacionForm
#     pk_url_kwarg = "pk"


#INCIDENCIAS
@login_required(login_url="/login/")
def Incidencias (request, pk_test):
    class valores:
        vcanton = ""
        vprovincia = Provincia.objects.get(codprovincia=pk_test)
        vcount = 0

    canton_list = Canton.objects.raw('select * from estructura_canton where estructura_canton.provincia_id=' + pk_test)

   #FILTRAR POR CANTON
    if request.method == "POST":
        if request.POST.get('canton') == "*":
            canton = ''
            print (canton)
        else:
            canton = ' and estructura_jrv.canton_id =' + request.POST.get('canton')
            print (canton)

        valores.vcanton = request.POST.get('canton')

        if 'validacion' in request.POST:
            cursor = connection.cursor()
            donde = request.session['qdonde']
            print("donde")
            # print(donde)
            # updateQuery = "update estructura_jrv e set para_validar=True from comparacion_votacion where  e.cod = comparacion_votacion.jrv_id and " + donde
            #  cursor.execute(updateQuery)
            print("Columna de escrutinio actualizada")
            mensaje = 'Jrv(s) añadidas para Validacion'
            context = {'valores': valores, 'canton_list': canton_list }
        else:
            donde = ' and estructura_jrv.provincia_id=' + pk_test + canton
    else:
        donde = ' and estructura_jrv.provincia_id=' + pk_test

    jrv_list = votacion.objects.raw('select * from estructura_jrv where estructura_jrv.incidencia = True ' + donde + ' order by fecha_incidencia DESC')
    valores.vcount = len(jrv_list)
    print(jrv_list)
    context = {'valores': valores, 'canton_list': canton_list, "jrv_list": jrv_list}
    return render(request, 'incidencias/incidencias.html', context)


#EDITAR INCIDENCIAS
@login_required(login_url="/login/")
def JRVViewIncidencia(request, pk):
    if request.method == "POST":
        # Guardado
        print (request.POST)
        pk = request.POST.get('jrvactual')
        q= JRV.objects.get(cod=pk)
        q.observaciones=request.POST.get('Observaciones')
        if request.POST.get('resuelta') == 'Se resolvio' :
            q.incidencia_resuelta = True
        else:
            q.incidencia_resuelta = False

        if request.POST.get('grave') == 'Incidencia Grave':
            q.incidencia_grave = True
        else:
            q.incidencia_grave = False
        q.save()
        response = redirect('/comparacion/incidencias/'+str(q.provincia.pk))
        return response

    votacion_list = votacion.objects.filter(jrv__cod=pk)
    jrvactual = JRV.objects.get(cod=pk)

    resuelta="null"
    grave="null"

    if jrvactual.incidencia_resuelta:
        resuelta="si"

    if jrvactual.incidencia_grave:
        grave="si"

    candidatos = partido.objects.filter(dignidad_id=1)
    context = {"votacion_list": votacion_list, 'jrvactual': jrvactual, 'resuelta': resuelta, 'grave': grave, 'candidatos': candidatos}
    return render(request, 'incidencias/edit_jrv_incidencia.html', context)


#VALIDACION PRESIDENTE
@login_required(login_url="/login/")
def Validacion_presidente(request, pk_test):
    class valores:
        vcanton = ""
        vprovincia = Provincia.objects.get(codprovincia=pk_test)
        vcount = 0

    canton_list = Canton.objects.raw('select * from estructura_canton where estructura_canton.provincia_id=' + pk_test)

    print("validacion")
    if request.method == "POST":
        if request.POST.get('canton') == "*":
            canton = ''
        else:
            canton = ' and estructura_jrv.canton_id =' + request.POST.get('canton')
        valores.vcanton = request.POST.get('canton')
        donde = ' and provincia_id=' + pk_test + canton
    else:
        donde = ' and estructura_jrv.provincia_id=' + pk_test

    jrv_list = JRV.objects.raw('select * from estructura_jrv where estructura_jrv.no_procede <> True and estructura_jrv.para_reclamar <> True and estructura_jrv.para_validar = True' + donde )   #  + ' order by maxdiff DESC'
    valores.vcount = len(jrv_list)
    print(jrv_list)
    context = {'valores': valores, 'canton_list': canton_list, "jrv_list": jrv_list}
    return render(request, 'validacion/validacion_presidente.html', context)


#VALIDACION EDIT PRESIDENTE
@login_required(login_url="/login/")
def JRVView(request, pk):
    if request.method == "POST":
        # Guardado
        print (request.POST)
        pk = request.POST.get('jrvactual')
        q= JRV.objects.get(cod=pk)
        q.observaciones=request.POST.get('Observaciones')
        if request.POST.get('reclamar') == 'para_reclamar' :
            q.para_reclamar = True
        if request.POST.get('reclamar') == 'No_procede':
            q.no_procede = True
        if request.POST.get('quitaron') != '':
            q.quitaron = request.POST.get('quitaron')
        if request.POST.get('pusieron') != '':
            q.pusieron = request.POST.get('pusieron')
        if request.POST.get('otroreclamo') != '':
            q.otro1 = request.POST.get('otroreclamo')
        q.save()
        response = redirect('/comparacion/validacion_presidente/'+str(q.provincia_id))
        return response

    print("version ultima actualizada")
    votacion_list = votacion.objects.raw("select * from comparacion_votacion where dignidad_id=1 and jrv_id='"+pk+"' order by comparacion_votacion.partido_id")
    jrvactual = JRV.objects.get(cod=pk)
    if jrvactual.para_reclamar == True:
        print("para reclamar")
        reclamar="si"
    else:
        if jrvactual.no_procede == True:
            print("No procede reclamo")
            reclamar="no"
        else:
            reclamar="null"

    provstr=str(jrvactual.provincia.nomprovincia).rstrip("\n")
    cantonstr = str(jrvactual.canton.nomcanton).rstrip("\n")
    if jrvactual.circunscripcion is None: circunstr = "0"
    else: circunstr = str(jrvactual.circunscripcion.codcircunscripcion)
    if jrvactual.zona is None: zonastr = "0"
    else: zonastr = str(jrvactual.zona.codzona)
    imagencne = requote_uri("https://impugnaciones.andresarauz.ec/images/1-PRESIDENTA-E%20Y%20VICEPRESIDENTA-E/" + str(jrvactual.provincia_id) +"-"+provstr+"/"+str(jrvactual.canton_id) +"-"+cantonstr + \
                "/" + str(jrvactual.provincia_id) + "_" +str(jrvactual.canton_id)+"_"+ circunstr +"_"+str(jrvactual.parroquia_id)+"_"+zonastr+"_"+str(jrvactual.numero)+str(jrvactual.genero)+"_"+str(jrvactual.noactapre)+"_I1.pdf")
    print(imagencne )

    class imagen:
        uno= jrvactual.acta_delegados
        dos = jrvactual.acta_delegados2
        tres = jrvactual.acta_delegados3

    context = {"votacion_list": votacion_list, 'jrvactual': jrvactual,  'reclamar': reclamar, 'imagen' :imagen, 'imagencne':imagencne}
    return render(request, 'validacion/validar_jrv.html', context  )


@login_required(login_url="/login/")
def Excel_Presidente(request, pk_test):
    response = HttpResponse(content_type='application/ms-excel')
    prov=str(Provincia.objects.get(codprovincia=pk_test)).rstrip("\n")
    response['Content-Disposition'] = 'attachment; filename="RECLAMACION_PRESIDENTE_'+prov+".xls"
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Nos Quitaron')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Canton-Circunscripcion-Parroquia-Zona-JRV', 'votos a reclamar' ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = JRV.objects.filter(para_validar=True, quitaron__isnull= False, provincia_id=pk_test).values_list('canton__nomcanton', 'circunscripcion__codcircunscripcion','parroquia__nomparroquia', 'zona__codzona', 'numero', 'genero', 'quitaron')
    total=0
    for row in rows:
        row_num += 1
        if row[1] is None: circ="0"
        else: circ = row[1]
        if row[3] is None: zone="0"
        else: zone = row[3]
        nombre=str(row[0])+"-"+str(circ) +"-"+str(row[2]) +"-"+str(zone) +"-"+str(row[4])+str(row[5])
        votos=row[6]
        total= total + int(votos)
        ws.write(row_num, 0, nombre, font_style)
        ws.write(row_num, 1, votos, font_style)
    ws.write(row_num+1, 0, "TOTAL", font_style)
    ws.write(row_num+1, 1, total, font_style)
    #hoja 2
    ws = wb.add_sheet('Nos Pusieron')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Canton-Circunscripcion-Parroquia-Zona-JRV', 'votos a reclamar']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = JRV.objects.filter(para_validar=True, pusieron__isnull=False, provincia_id=pk_test).values_list('canton__nomcanton',
                                                                                     'circunscripcion__codcircunscripcion',
                                                                                     'parroquia__nomparroquia',
                                                                                     'zona__codzona', 'numero',
                                                                                     'genero', 'pusieron')
    total = 0
    for row in rows:
        row_num += 1
        if row[1] is None:
            circ = "0"
        else:
            circ = row[1]
        if row[3] is None:
            zone = "0"
        else:
            zone = row[3]
        nombre = str(row[0]) + "-" + str(circ) + "-" + str(row[2]) + "-" + str(zone) + "-" + str(row[4]) + str(row[5])
        votos = row[6]
        total = total + int(votos)
        ws.write(row_num, 0, nombre, font_style)
        ws.write(row_num, 1, votos, font_style)
    ws.write(row_num + 1, 0, "TOTAL", font_style)
    ws.write(row_num + 1, 1, total, font_style)
    # hoja 3
    ws = wb.add_sheet('Otras Reclamaciones')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Canton-Circunscripcion-Parroquia-Zona-JRV', 'motivo de reclamo']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = JRV.objects.filter(para_validar=True, otro1__isnull=False, provincia_id=pk_test).values_list('canton__nomcanton',
                                                                                     'circunscripcion__codcircunscripcion',
                                                                                     'parroquia__nomparroquia',
                                                                                     'zona__codzona', 'numero',
                                                                                     'genero', 'otro1')
    total = 0
    for row in rows:
        row_num += 1
        if row[1] is None:
            circ = "0"
        else:
            circ = row[1]
        if row[3] is None:
            zone = "0"
        else:
            zone = row[3]
        nombre = str(row[0]) + "-" + str(circ) + "-" + str(row[2]) + "-" + str(zone) + "-" + str(row[4]) + str(row[5])
        votos = row[6]
        ws.write(row_num, 0, nombre, font_style)
        ws.write(row_num, 1, votos, font_style)

    wb.save(response)
    return response


@login_required(login_url="/login/")
def Validacion_Random(request, pk_test):

        class valores:
            vcolumna1 = "delegados"
            vcolumna2 = "cne1"
            vcandidato = "7"
            voperador = "lt"
            vcanton = ""
            vprovincia = Provincia.objects.get(codprovincia=pk_test)
            vcount = 0
            vdonde = ''

        mensaje=''
        candidatos = partido.objects.filter(dignidad_id=1)
        canton_list = Canton.objects.raw('select * from estructura_canton where estructura_canton.provincia_id='+pk_test)

        if request.method=="POST":
            columna1=request.POST.get('columna1')
            columna2 = request.POST.get('columna2')
            operador = request.POST.get('operador')
            candidatopost = request.POST.get('candidato')
            if request.POST.get('canton') == "*" :
                canton = ''
            else:
                canton = ' and comparacion_votacion.canton_id =' + request.POST.get('canton')

            if operador == "lt":
                opr = '<'
            if operador == "gt":
                opr = '>'
            if operador == "!=":
                opr = '!='

            valores.vcolumna1 = columna1
            valores.vcolumna2 = columna2
            valores.vcandidato = candidatopost
            valores.voperador = operador
            valores.vcanton=request.POST.get('canton')

            if 'validacion' in request.POST:
                cursor = connection.cursor()
                donde =request.session['qdonde']
                print(donde)
                updateQuery = "update estructura_jrv e set para_validar=True from comparacion_votacion where  e.cod = comparacion_votacion.jrv_id and " + donde
                cursor.execute(updateQuery)
                print("Columna de escrutinio actualizada")
                mensaje = 'Jrv(s) añadidas para Validacion'
                context = {'valores': valores, 'canton_list': canton_list,  'candidatos': candidatos, }
            else:
                donde='comparacion_votacion.candidato_id = ' + candidatopost +' and comparacion_votacion.' + columna1 + ' ' + opr + ' comparacion_votacion.' + columna2 + ' and comparacion_votacion.provincia_id='+pk_test+ canton
        else:
            donde='comparacion_votacion.delegados < comparacion_votacion.cne1 and comparacion_votacion.provincia_id='+pk_test

        request.session['qdonde'] = donde
        votacion_list = votacion.objects.raw('select * from comparacion_votacion where '+ donde)
        valores.vcount = len(votacion_list)
        print("antes de enviar siguio")
        context = { 'valores': valores, 'canton_list': canton_list, "votacion_list": votacion_list, 'candidatos': candidatos , 'mensaje' : mensaje }
        return render(request, 'consulta/consulta_presidente.html', context)


##OTRAS CONSULTAS _PRESIDENTE
@login_required(login_url="/login/")
def Consulta_presidente(request, pk_test):

        class valores:
            vcolumna1 = "delegados"
            vcolumna2 = "cne1"
            vcandidato = "*"
            voperador = "lt"
            vcanton = ""
            vprovincia = Provincia.objects.get(codprovincia=pk_test)
            vcount = 0
            vdonde = ''

        mensaje=''
        partidos = partido.objects.filter(dignidad_id=1)
        canton_list = Canton.objects.raw('select * from estructura_canton where estructura_canton.provincia_id='+pk_test)

        if request.method=="POST":
            print(request.POST)
            columna1=request.POST.get('columna1')
            columna2 = request.POST.get('columna2')
            operador = request.POST.get('operador')
            if request.POST.get('canton') == "*" :
                canton = ''
            else:
                canton = ' and comparacion_votacion.canton_id =' + request.POST.get('canton')

            if request.POST.get('partidosselect') == "*":
                candidato = ''
            else:
                candidato = 'comparacion_votacion.partido_id = ' + request.POST.get('partidosselect')

            if operador == "lt":
                opr = '<'
            if operador == "gt":
                opr = '>'
            if operador == "!=":
                opr = '!='

            valores.vcolumna1 = columna1
            valores.vcolumna2 = columna2
            valores.vcandidato = request.POST.get('partidosselect')
            valores.voperador = operador
            valores.vcanton=request.POST.get('canton')

            if 'validacion' in request.POST:
                            cursor = connection.cursor()
                            donde =request.session['qdonde']
                            print(donde)
                            updateQuery = "update estructura_jrv e set para_validar=True from comparacion_votacion where  e.cod = comparacion_votacion.jrv_id and " + donde
                            cursor.execute(updateQuery)
                            mensaje = 'Jrv(s) añadidas para Validacion'
                            context = {'valores': valores, 'canton_list': canton_list,  'candidatos': partidos, }

            donde = 'comparacion_votacion.' + columna1 + ' ' + opr + ' comparacion_votacion.' + columna2 + ' and comparacion_votacion.provincia_id=' + pk_test + canton
        else:
            donde='comparacion_votacion.delegados < comparacion_votacion.cne1 and comparacion_votacion.dignidad_id=1 and comparacion_votacion.provincia_id='+pk_test

        request.session['qdonde'] = donde
        votacion_list = votacion.objects.raw('select * from comparacion_votacion where '+ donde)
        valores.vcount = len(votacion_list)
        print("antes de enviar siguio")
        context = { 'valores': valores, 'canton_list': canton_list, "votacion_list": votacion_list, 'candidatos': partidos , 'mensaje' : mensaje }
        return render(request, 'consulta/consulta_presidente.html', context)


# EDITAR OTRAS CONSULTAS PRESIDENTE
@login_required(login_url="/login/")
def VotacionModalView(request, pk):
    class valores:
        vcolumna1 = "delegados"
        vcolumna2 = "cne1"
        vcandidato = "candidato1"
        voperador = "lt"
        vcanton = ""
        vcounter = 1000

    mesa = pk[0:15]
    votacion_list = votacion.objects.filter(jrv_id=mesa,dignidad_id=1).order_by('partido')
    jrvcandidato = votacion.objects.get(cod=pk)
    candidatos = partido.objects.filter(dignidad_id=1)
    context = {"votacion_list": votacion_list, 'jrvcandidato': jrvcandidato, 'candidatos': candidatos,
               'valores': valores}
    return render(request, 'consulta/read_jrv.html', context)
