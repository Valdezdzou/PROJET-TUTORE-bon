# Generated by Django 4.2.2 on 2023-06-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_fichier_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichier',
            name='date_de_modification',
            field=models.DateField(blank=True),
        ),
    ]
