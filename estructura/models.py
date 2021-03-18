from django.db import models
from django.urls import reverse


class Provincia(models.Model):
    # Fields
    codprovincia = models.IntegerField(primary_key=True)
    nomprovincia = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

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
        verbose_name = 'Circunscripción'
        verbose_name_plural = 'Circunscripciones'

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
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantones'

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
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'

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
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

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
        verbose_name = 'Recinto'
        verbose_name_plural = 'Recintos'

    def __str__(self):
        return str(self.nomrecinto)

    def get_absolute_url(self):
        return reverse("estructura_Recinto_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Recinto_update", args=(self.pk,))


class Alert(models.Model):
    name = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'

    def __str__(self):
        return self.name


class JRV(models.Model):
    # Relationships
    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)
    canton = models.ForeignKey("estructura.Canton", on_delete=models.CASCADE)
    parroquia = models.ForeignKey("estructura.Parroquia", on_delete=models.CASCADE)
    zona = models.ForeignKey("estructura.Zona", on_delete=models.CASCADE, null=True)
    recinto = models.ForeignKey("estructura.Recinto", on_delete=models.CASCADE)
    alerts = models.ManyToManyField(Alert)

    # Fields
    cod = models.CharField(max_length=30, primary_key=True)
    codcne = models.IntegerField(null=True)
    numero = models.IntegerField()
    genero = models.CharField(max_length=1)
    num_electores = models.IntegerField()
    quitaron = models.IntegerField(null=True)
    pusieron = models.IntegerField(null=True)
    appsufragantes = models.IntegerField(null=True)
    appblancos = models.IntegerField(null=True)
    appnulos = models.IntegerField(null=True)
    app_arauz = models.IntegerField(null=True)
    app_lasso = models.IntegerField(null=True)
    cnesufragantes = models.IntegerField(null=True)
    cneblancos = models.IntegerField(null=True)
    cnenulos = models.IntegerField(null=True)
    cne_arauz = models.IntegerField(null=True)
    cne_lasso = models.IntegerField(null=True)
    old_cne_sufragantes = models.IntegerField(null=True)
    old_cne_blancos = models.IntegerField(null=True)
    old_cne_nulos = models.IntegerField(null=True)
    old_cne_arauz = models.IntegerField(null=True)
    old_cne_lasso = models.IntegerField(null=True)
    difference_arauz = models.IntegerField(null=True)
    difference_lasso = models.IntegerField(null=True)
    para_validar = models.BooleanField(default=False)
    difnum1 = models.BooleanField(default=False)
    otro1 = models.CharField(max_length=30, null=True)
    no_procede = models.BooleanField(default=False)
    para_reclamar = models.BooleanField(default=False)
    incidencia = models.BooleanField(default=False)
    fecha_incidencia = models.DateTimeField(null=True)
    incidencia_grave = models.BooleanField(default=False)
    incidencia_resuelta = models.BooleanField(null=True)
    observaciones = models.TextField()
    telefonos = models.TextField()
    acta_delegados = models.CharField(max_length=255, null=True)
    acta_cne = models.CharField(max_length=255, null=True)
    acta_cnerecuento = models.CharField(max_length=255, null=True)
    noactapre = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'JRV'
        verbose_name_plural = 'JRVs'

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
        verbose_name = 'Dignidad'
        verbose_name_plural = 'Dignidades'

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
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

    def __str__(self):
        return str(self.nompartido)

    def get_absolute_url(self):
        return reverse("estructura_partido_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_partido_update", args=(self.pk,))
