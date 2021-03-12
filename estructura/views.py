from django.views import generic
from . import models
from . import forms
from dal import autocomplete


class GParroquiaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #   if not self.request.user.is_authenticated():
        #      return models.Parroquia.objects.none()

        qs = models.Parroquia.objects.all()

        canton = self.forwarded.get('canton', None)


        if canton:
            qs = qs.filter(canton_id=canton)

        if self.q:
            qs = qs.filter(NOM_PARROQUIA__contains=self.q)

        return qs


class GZonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #   if not self.request.user.is_authenticated():
        #      return models.Parroquia.objects.none()

        qs = models.Zona.objects.all()

        parroquia = self.forwarded.get('parroquia', None)
        print(parroquia)

        if parroquia:
            qs = qs.filter(parroquia_id=parroquia)

        if self.q:
            qs = qs.filter(NOM_ZONA__contains=self.q)

        return qs


class GCantonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #   if not self.request.user.is_authenticated():
        #      return models.Parroquia.objects.none()

        qs = models.Canton.objects.all()

        provincia = self.forwarded.get('provincia', None)
        print(provincia)

        if provincia:
            qs = qs.filter(provincia_id=provincia)

        if self.q:
            qs = qs.filter(NOM_CANTON__contains=self.q)

        return qs


class GProvinciaAutocomplete(autocomplete.Select2QuerySetView):
        def get_queryset(self):
            # Don't forget to filter out results depending on the visitor !
            #   if not self.request.user.is_authenticated():
            #      return models.Parroquia.objects.none()
            qs = models.Provincia.objects.all()

            if self.q:
                qs = qs.filter(NOM_PROVINCIA__icontains=self.q)

            return qs

class RecintoListView(generic.ListView):
    model = models.Recinto
    form_class = forms.RecintoForm


class RecintoCreateView(generic.CreateView):
    model = models.Recinto
    form_class = forms.RecintoForm


class RecintoDetailView(generic.DetailView):
    model = models.Recinto
    form_class = forms.RecintoForm


class RecintoUpdateView(generic.UpdateView):
    model = models.Recinto
    form_class = forms.RecintoForm
    pk_url_kwarg = "pk"

class CantonListView(generic.ListView):
    model = models.Canton
    form_class = forms.CantonForm

class CantonCreateView(generic.CreateView):
    model = models.Canton
    form_class = forms.CantonForm

class CantonDetailView(generic.DetailView):
    model = models.Canton
    form_class = forms.CantonForm

class CantonUpdateView(generic.UpdateView):
    model = models.Canton
    form_class = forms.CantonForm
    pk_url_kwarg = "pk"

class ZonaListView(generic.ListView):
    model = models.Zona
    form_class = forms.ZonaForm

class ZonaCreateView(generic.CreateView):
    model = models.Zona
    form_class = forms.ZonaForm

class ZonaDetailView(generic.DetailView):
    model = models.Zona
    form_class = forms.ZonaForm

class ZonaUpdateView(generic.UpdateView):
    model = models.Zona
    form_class = forms.ZonaForm
    pk_url_kwarg = "pk"

class ParroquiaListView(generic.ListView):
    model = models.Parroquia
    form_class = forms.ParroquiaForm

class ParroquiaCreateView(generic.CreateView):
    model = models.Parroquia
    form_class = forms.ParroquiaForm

class ParroquiaDetailView(generic.DetailView):
    model = models.Parroquia
    form_class = forms.ParroquiaForm

class ParroquiaUpdateView(generic.UpdateView):
    model = models.Parroquia
    form_class = forms.ParroquiaForm
    pk_url_kwarg = "pk"

class ProvinciaListView(generic.ListView):
    model = models.Provincia
    form_class = forms.ProvinciaForm

class ProvinciaCreateView(generic.CreateView):
    model = models.Provincia
    form_class = forms.ProvinciaForm

class ProvinciaDetailView(generic.DetailView):
    model = models.Provincia
    form_class = forms.ProvinciaForm

class ProvinciaUpdateView(generic.UpdateView):
    model = models.Provincia
    form_class = forms.ProvinciaForm
    pk_url_kwarg = "pk"
