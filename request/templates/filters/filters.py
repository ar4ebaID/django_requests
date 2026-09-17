import django_filters
from django_filters import DateTimeFilter
from request.models import *


class ReportFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name='Request_date', lookup_expr="gte")
    end_date = DateTimeFilter(field_name='Request_date', lookup_expr="lte")

    class Meta:
        model = Request
        fields = ['Lecture_hall', 'Work', 'Performer']


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        fields = ('id', 'Customers_full_name', 'Lecture_hall', 'Condition')