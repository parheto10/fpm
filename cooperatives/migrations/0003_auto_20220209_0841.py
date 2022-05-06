# Generated by Django 3.1.7 on 2022-02-09 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0008_intitule_formation'),
        ('cooperatives', '0002_auto_20220209_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='niveauformateur',
            field=models.CharField(default=1, max_length=100, verbose_name='NIVEAU ETUDE FORMATEUR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formation',
            name='structureformateur',
            field=models.CharField(default=1, max_length=100, verbose_name='STRUCTURE FORMATEUR'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formation',
            name='campagne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.campagne'),
        ),
    ]
