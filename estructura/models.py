from django.db import models
from django.urls import reverse


class Provincia(models.Model):

    # Fields
    codprovincia = models.IntegerField(primary_key=True)
    nomprovincia = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
            return str(self.nomprovincia)
    def get_absolute_url(self):
        return reverse("estructura_Provincia_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Provincia_update", args=(self.pk,))


class Circunscripcion(models.Model):

    # Relationships
    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)

    # Fields
    codcircunscripcion = models.IntegerField()
    nomcircunscripcion = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.nomcircunscripcion)

    def get_provincia(self):
        return str(self.provincia.nomprovincia)

    get_provincia.admin_order_field = 'provincia'


class Canton(models.Model):

    # Relationships
    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)

    # Fields
    codcanton = models.IntegerField(primary_key=True)
    nomcanton = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.nomcanton)

    def get_provincia(self):
        return str(self.provincia.nomprovincia)

    get_provincia.admin_order_field = 'provincia'

    def get_absolute_url(self):
        return reverse("estructura_Canton_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Canton_update", args=(self.pk,))


class Parroquia(models.Model):

    # Relationships
    canton = models.ForeignKey("estructura.Canton", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)

    # Fields
    codparroquia = models.IntegerField(primary_key=True)
    nomparroquia = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.nomparroquia)

    def get_absolute_url(self):
        return reverse("estructura_Parroquia_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Parroquia_update", args=(self.pk,))


class Zona(models.Model):

    # Relationships
    parroquia = models.ForeignKey("estructura.Parroquia", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)

    # Fields
    codzona = models.IntegerField()
    nomzona = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.codzona)

    def get_absolute_url(self):
        return reverse("estructura_Zona_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Zona_update", args=(self.pk,))


class Recinto(models.Model):

    # Relationships
    parroquia = models.ForeignKey("estructura.Parroquia", on_delete=models.CASCADE)
    zona = models.ForeignKey("estructura.Zona", on_delete=models.CASCADE, null=True)

    # Fields
    codrecinto = models.IntegerField(primary_key=True)
    nomrecinto = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.nomrecinto)

    def get_absolute_url(self):
        return reverse("estructura_Recinto_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Recinto_update", args=(self.pk,))


class JRV(models.Model):

    # Relationships
    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)
    canton = models.ForeignKey("estructura.Canton", on_delete=models.CASCADE)
    parroquia = models.ForeignKey("estructura.Parroquia", on_delete=models.CASCADE)
    zona = models.ForeignKey("estructura.Zona", on_delete=models.CASCADE, null=True)
    recinto = models.ForeignKey("estructura.Recinto", on_delete=models.CASCADE)

    # Fields
    cod = models.CharField(max_length=30, primary_key=True)
    codcne = models.IntegerField(null=True)
    numero=models.IntegerField()
    genero=models.CharField(max_length=1)
    num_electores=models.IntegerField()
    quitaron = models.IntegerField(null=True)
    pusieron = models.IntegerField(null=True)
    quitaron7 = models.IntegerField(null=True)
    pusieron7 = models.IntegerField(null=True)
    quitaron8 = models.IntegerField(null=True)
    pusieron8 = models.IntegerField(null=True)
    quitaron9 = models.IntegerField(null=True)
    pusieron9 = models.IntegerField(null=True)
    appsufragantes = models.IntegerField(null=True)
    appblancos = models.IntegerField(null=True)
    appnulos = models.IntegerField(null=True)
    digitasufragantes = models.IntegerField(null=True)
    digitablancos = models.IntegerField(null=True)
    digitanulos = models.IntegerField(null=True)
    cnesufragantes = models.IntegerField(null=True)
    cneblancos = models.IntegerField(null=True)
    cnenulos = models.IntegerField(null=True)
    tmpdiff1 = models.IntegerField(null=True)
    tmpdiff2 = models.IntegerField(null=True)
    maxdiff = models.IntegerField(null=True)
    maxdiffnal= models.IntegerField(null=True)
    maxdiffprov= models.IntegerField(null=True)
    maxdiffand= models.IntegerField(null=True)
    para_validar = models.BooleanField(default=False)
    para_validar7 = models.BooleanField(default=False)
    para_validar8 = models.BooleanField(default=False)
    para_validar9 = models.BooleanField(default=False)
    difnum1= models.BooleanField(default=False)
    difnum7= models.BooleanField(default=False)
    difnum8= models.BooleanField(default=False)
    difnum9 = models.BooleanField(default=False)
    otro1 = models.CharField(max_length=30,null=True)
    otro7 = models.CharField(max_length=30,null=True)
    otro8 = models.CharField(max_length=30,null=True)
    otro9 = models.CharField(max_length=30,null=True)
    no_procede = models.BooleanField(default=False)
    para_reclamar = models.BooleanField(default=False)
    no_procede7 = models.BooleanField(default=False)
    para_reclamar7 = models.BooleanField(default=False)
    no_procede8 = models.BooleanField(default=False)
    para_reclamar8 = models.BooleanField(default=False)
    no_procede9 = models.BooleanField(default=False)
    para_reclamar9 = models.BooleanField(default=False)
    incidencia= models.BooleanField(default=False)
    fecha_incidencia=models.DateTimeField(null=True)
    incidencia_grave = models.BooleanField(default=False)
    incidencia_resuelta= models.BooleanField(null=True)
    observaciones = models.TextField()
    telefonos = models.TextField()
    acta_delegados = models.CharField(max_length=255, null=True)
    acta_delegados2 = models.CharField(max_length=255, null=True)
    acta_delegados3 = models.CharField(max_length=255, null=True)
    acta_delegadosnal = models.CharField(max_length=255, null=True)
    acta_delegadosnal2 = models.CharField(max_length=255, null=True)
    acta_delegadosnal3 = models.CharField(max_length=255, null=True)
    acta_delegadosprov = models.CharField(max_length=255, null=True)
    acta_delegadosprov2 = models.CharField(max_length=255, null=True)
    acta_delegadosprov3 = models.CharField(max_length=255, null=True)
    acta_delegadosand = models.CharField(max_length=255, null=True)
    acta_delegadosand2 = models.CharField(max_length=255, null=True)
    acta_delegadosand3 = models.CharField(max_length=255, null=True)
    acta_copia = models.CharField(max_length=255, null=True)
    acta_copia2 = models.CharField(max_length=255, null=True)
    acta_copia3 = models.CharField(max_length=255, null=True)
    acta_copianal = models.CharField(max_length=255, null=True)
    acta_copianal2 = models.CharField(max_length=255, null=True)
    acta_copianal3 = models.CharField(max_length=255, null=True)
    acta_copiaprov = models.CharField(max_length=255, null=True)
    acta_copiaprov2 = models.CharField(max_length=255, null=True)
    acta_copiaprov3 = models.CharField(max_length=255, null=True)
    acta_copiaand = models.CharField(max_length=255, null=True)
    acta_copiaand2 = models.CharField(max_length=255, null=True)
    acta_copiaand3 = models.CharField(max_length=255, null=True)
    acta_cne = models.CharField(max_length=255, null=True)
    acta_cnerecuento = models.CharField(max_length=255, null=True)
    noactapre=models.IntegerField(null=True)
    noactanal=models.IntegerField(null=True)
    noactapro=models.IntegerField(null=True)
    noactaand=models.IntegerField(null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("estructura_JRV_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_JRV_update", args=(self.pk,))


class dignidad(models.Model):

    # Fields
    coddignidad = models.IntegerField(primary_key=True)
    nomdignidad = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.nomdignidad)

    def get_absolute_url(self):
        return reverse("estructura_dignidad_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_dignidad_update", args=(self.pk,))


class partido(models.Model):

    # Fields
    codpartido = models.IntegerField()
    nompartido = models.CharField(max_length=255)

    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)
    dignidad = models.ForeignKey("estructura.dignidad", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.nompartido)

    def get_absolute_url(self):
        return reverse("estructura_partido_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_partido_update", args=(self.pk,))
