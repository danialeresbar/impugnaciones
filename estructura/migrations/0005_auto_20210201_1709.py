# Generated by Django 2.2.17 on 2021-02-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0004_auto_20210201_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='jrv',
            name='acta_cnerecuento',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_copiaand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_copianal',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_copiaprov',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_delegadosand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_delegadosnal',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='acta_delegadosprov',
            field=models.CharField(max_length=255, null=True),
        ),
    ]