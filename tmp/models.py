from django.db import models
from postgres_copy import CopyManager


class escrutinio1(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class escrutinio2(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class escrutinio3(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class escrutinio4(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class aplicacion(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class old_cne(models.Model):
    # Fields
    uid = models.CharField(max_length=30, primary_key=True)
    cod_junta = models.IntegerField(null=True)
    sufragantes = models.IntegerField(null=True)
    blancos = models.IntegerField(null=True)
    nulos = models.IntegerField(null=True)
    arauz_votes = models.IntegerField(null=True)
    lasso_votes = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
