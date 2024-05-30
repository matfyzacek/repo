# Generated by Django 5.0.6 on 2024-05-24 08:48

from django.db import migrations

def insert_data(apps,schema_editor):
    Projects=apps.get_model("portfolio","Project")
    TypeProjects=apps.get_model("portfolio","TypeProject")
    bjj=TypeProjects.objects.first()
    for index in range(6,5000):
        Projects.objects.create(name=f"Project {index}",description="",image="static/7400_kj0NPyG.png",mycode=f"https://{index}.com",typ=bjj)

class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0010_alter_project_description_alter_project_tagy"),
    ]

    operations = [migrations.RunPython(insert_data)]
