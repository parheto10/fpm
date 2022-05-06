# Generated by Django 3.1.7 on 2022-02-15 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0009_auto_20220214_1748'),
        ('cooperatives', '0012_auto_20220215_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPlantingRemplacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_plante', models.PositiveIntegerField(default=0, verbose_name='QTE recu')),
                ('espece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.espece')),
                ('planting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperatives.planting')),
            ],
            options={
                'verbose_name': 'details planting remplacement',
                'verbose_name_plural': 'DETAILS PLANTINGS APRES REMPLACEMENT',
            },
        ),
        migrations.AddField(
            model_name='monitoringespece',
            name='detailplantingremplacement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cooperatives.detailplantingremplacement'),
        ),
    ]