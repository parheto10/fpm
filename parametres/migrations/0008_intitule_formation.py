# Generated by Django 3.1.7 on 2022-01-27 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0007_auto_20220107_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intitule_Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.projet')),
            ],
            options={
                'verbose_name': 'theme formation',
                'verbose_name_plural': 'THEMES DES FORMATIONS',
            },
        ),
    ]
