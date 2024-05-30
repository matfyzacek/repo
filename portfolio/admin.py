from django.contrib import admin
from portfolio.models import Project,TypeProject,TypeURL,TypeTag
from users.models import Editor
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=("name","typ","description","image")
    search_fields=("name","description")
    list_filter=()
    list_per_page=100
@admin.register(TypeProject)
class TypeProjeee(MarkdownxModelAdmin):
    list_display=("name","description")
    search_fields=("name","description")
    list_filter=("name","description")
    list_per_page=10
@admin.register(TypeURL)
class TypeURLEE(admin.ModelAdmin):
    list_display=("name","ikona")
    search_fields=("name","ikona")
    list_filter=("name","ikona")
    list_per_page=10
@admin.register(TypeTag)
class TypeURLEE(admin.ModelAdmin):
    list_display=("name","color")
    search_fields=("name","color")
    list_filter=("name","color")
    list_per_page=10
@admin.register(Editor)
class TypeEDITOR(admin.ModelAdmin):
    list_display=("user",)
    search_fields=("user",)
    list_filter=("user",)
    list_per_page=10
