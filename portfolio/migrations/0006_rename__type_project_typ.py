# Generated by Django 5.0.6 on 2024-05-22 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0005_typeproject_alter_project_created_at_project__type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="_type",
            new_name="typ",
        ),
    ]
