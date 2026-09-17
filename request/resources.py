from .models import *
from import_export import resources


class ReportResources(resources.ModelResource):
    class Meta:
        model = Request