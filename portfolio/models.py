from django.db import models
from django.contrib import admin
from portfolio.managers import ProjectManager
from colorfield.fields import ColorField
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
class TypeProject(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Jméno:")
    description=models.TextField(max_length=100,verbose_name="Popisek:")
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name="Typ projektu"
        verbose_name_plural="Typy projektů"
class TypeURL(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Název služby:")
    ikona=models.ImageField(upload_to="static/",verbose_name="Ikona: ")
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name="Typ repozitáře"
        verbose_name_plural="Typy repozitářů"
class TypeTag(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Jméno")
    color=ColorField(max_length=100,default="#FF00000",verbose_name="Barva:")
    def __str__(self):
        return "Položka "+str(self.name)
    class Meta:
        verbose_name="TAG"
        verbose_name_plural="TAGY"
class Project(models.Model):
    objects=ProjectManager()
    id=models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="jméno",max_length=100)
    description=MarkdownxField(max_length=1000,verbose_name="popisek",blank=True,null=True)
    image=models.ImageField(upload_to="static/",verbose_name="Obrázek")
    mycode=models.URLField(verbose_name="URL mého projektu.",blank=True,null=True)
    created_at=models.DateTimeField(verbose_name="Čas vytvoření:",blank=True,null=True,auto_now=True)
    typ=models.ForeignKey(TypeProject,on_delete=models.RESTRICT)
    typ_sluzby_projektu=models.ForeignKey(TypeTag,blank=True,null=True,on_delete=models.RESTRICT)
    tagy=models.ManyToManyField(TypeTag,related_name="aaa",verbose_name="Tagy",null=True,blank=True)
    @property
    def get_pretty_description(self):
        return markdownify(self.description)
    def __str__(self):
        return "Položka "+str(self.name)
    class Meta:
        verbose_name="Projekt"
        verbose_name_plural="Projekty"
