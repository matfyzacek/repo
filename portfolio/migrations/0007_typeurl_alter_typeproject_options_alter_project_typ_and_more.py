# Generated by Django 5.0.6 on 2024-05-23 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0006_rename__type_project_typ"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeURL",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Název služby:"),
                ),
                (
                    "ikona",
                    models.ImageField(upload_to="static/", verbose_name="Ikona: "),
                ),
            ],
            options={
                "verbose_name": "Typ repozitáře",
                "verbose_name_plural": "Typy repozitářů",
            },
        ),
        migrations.AlterModelOptions(
            name="typeproject",
            options={
                "verbose_name": "Typ projektu",
                "verbose_name_plural": "Typy projektů",
            },
        ),
        migrations.AlterField(
            model_name="project",
            name="typ",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="portfolio.typeproject"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="typ_sluzby_projektu",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="portfolio.typeurl",
            ),
        ),
    ]