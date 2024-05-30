from typing import Any
from django.views.generic import TemplateView
from datetime import datetime
from portfolio.models import Project
import time
class BasePage(TemplateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context["actual_date"]=datetime.now()
        context["time"]=time.time()
        context["kwg"]="Fuck you"
        return context

class AboutView(BasePage):
    template_name = "home.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data()
        context["projects"]=Project.objects.all()
        print(self.request.user.user)
        return context
class Epilepsie(BasePage):
    template_name = "epilepsie.html"
class InfoPage(BasePage):
    template_name = "detail.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context["project"]=Project.objects.get(id=context.get("project_id"))
        return context