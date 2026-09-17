from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('autocomplete_cus', autocomplete_cus, name='autocomplete_cus'),
    path('autocomplete_lec', autocomplete_lec, name='autocomplete_lec'),
    path('create/', create_request),
    path('<str:pk>/update', RequestUpdate),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_user),
    path('report', Report),
    path('report/export_excel', export_excel, name='export_excel'),
]