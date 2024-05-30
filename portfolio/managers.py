from django.db import models
from django.utils.timezone import now
class ProjectManager(models.Manager):
    def get_projects_this_year():
        year=year or now().year
        return self.get_queryset().filter(created_at__year=year)