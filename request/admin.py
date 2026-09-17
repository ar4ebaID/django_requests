from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin


class RequestAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'Customers_full_name', 'Lecture_hall', 'Description', 'Work', 'Performer', 'Comment',
                    'Files', 'Request_date', 'Condition')
    search_fields = ('id', 'Customers_full_name', 'Lecture_hall')
    list_display_links = ('id',)


admin.site.register(Request, RequestAdmin)
admin.site.register(Condition_list, SimpleHistoryAdmin)
admin.site.register(Type_of_work_list, SimpleHistoryAdmin)
admin.site.register(Full_name_of_the_performer_list, SimpleHistoryAdmin)
