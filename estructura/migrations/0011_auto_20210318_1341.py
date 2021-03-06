# Generated by Django 2.2.16 on 2021-03-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0010_auto_20210316_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jrv',
            old_name='digitablancos',
            new_name='app_arauz',
        ),
        migrations.RenameField(
            model_name='jrv',
            old_name='digitanulos',
            new_name='app_lasso',
        ),
        migrations.RenameField(
            model_name='jrv',
            old_name='digitasufragantes',
            new_name='cne_arauz',
        ),
        migrations.RenameField(
            model_name='jrv',
            old_name='maxdiff',
            new_name='cne_lasso',
        ),
        migrations.RenameField(
            model_name='jrv',
            old_name='tmpdiff1',
            new_name='difference_arauz',
        ),
        migrations.RenameField(
            model_name='jrv',
            old_name='tmpdiff2',
            new_name='difference_lasso',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_copia',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_copia2',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_copia3',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegados2',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegados3',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosand',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosand2',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosand3',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosnal',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosnal2',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosnal3',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosprov',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosprov2',
        ),
        migrations.RemoveField(
            model_name='jrv',
            name='acta_delegadosprov3',
        ),
        migrations.AddField(
            model_name='jrv',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jrv',
            name='old_cne_arauz',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='old_cne_blancos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='old_cne_lasso',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='old_cne_nulos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jrv',
            name='old_cne_sufragantes',
            field=models.IntegerField(null=True),
        ),
    ]
