# Generated by Django 3.1.7 on 2022-02-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0009_auto_20220214_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prime',
            name='libelle',
            field=models.CharField(max_length=250),
        ),
    ]