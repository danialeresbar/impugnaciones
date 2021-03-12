from django.db import models
from django.urls import reverse


class votacion(models.Model):
    # Relationships
    provincia = models.ForeignKey("estructura.Provincia", on_delete=models.CASCADE)
    circunscripcion = models.ForeignKey("estructura.Circunscripcion", on_delete=models.CASCADE, null=True)
    canton = models.ForeignKey("estructura.Canton", on_delete=models.CASCADE)
    parroquia = models.ForeignKey("estructura.Parroquia", on_delete=models.CASCADE)
    zona = models.ForeignKey("estructura.Zona", on_delete=models.CASCADE, null=True)
    recinto = models.ForeignKey("estructura.Recinto", on_delete=models.CASCADE)
    dignidad = models.ForeignKey("estructura.dignidad", on_delete=models.CASCADE)
    partido = models.ForeignKey("estructura.partido", on_delete=models.CASCADE)
    jrv = models.ForeignKey("estructura.JRV", on_delete=models.CASCADE)

    # Fields
    cod = models.CharField(max_length=30, primary_key=True)
    acta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    delegados = models.IntegerField(null=True)
    app_digitacion = models.IntegerField(null=True)
    conteo_rapido_cne = models.IntegerField(null=True)
    digitalizacion_cne = models.IntegerField(null=True)
    cne1 = models.IntegerField(null=True)
    ocr_nuestro_actas_cne = models.IntegerField(null=True)
    cne2 = models.IntegerField(null=True)
    cne3 = models.IntegerField(null=True)
    cne4 = models.IntegerField(null=True)
    diff1 = models.IntegerField(null=True)
    diff2 = models.IntegerField(null=True)
    diff3 = models.IntegerField(null=True)
    diff4 = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Votación'
        verbose_name_plural = 'Votaciones'
        ordering = ["cod"]

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("comparacion_votacion_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("comparacion_votacion_update", args=(self.pk,))


class fantasma(models.Model):
    # Fields
    uid = models.CharField(max_length=30)
    votos = models.IntegerField(null=True)
    origen = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name = 'Fantasma'
        verbose_name_plural = 'Fantasmas'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("comparacion_fantasma_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("comparacion_fantasma_votacion_update", args=(self.pk,))
