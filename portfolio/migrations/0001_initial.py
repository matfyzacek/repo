# Generated by Django 5.0.6 on 2024-05-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.ImageField(
                        upload_to="portfolio/images/", verbose_name="Obrázek"
                    ),
                ),
            ],
        ),
    ]
