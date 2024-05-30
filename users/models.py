from django.db import models

class Editor(models.Model):
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE,related_name="EDITOR")