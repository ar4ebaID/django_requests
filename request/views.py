import datetime
import xlwt
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import Create
from .models import *
from request.templates.filters.filters import ReportFilter, RequestFilter
from django.contrib.auth.decorators import login_required, permission_required
from .tasks import send_telegram_message_async


@login_required(login_url='login/')
@permission_required('request.view_request')
def index(request):

    requests = Request.objects.all()
    condition = Condition_list.objects.all()
    myFilter = RequestFilter(request.GET, queryset=requests)
    requests = myFilter.qs

    # search by single word
    search_query = request.GET.get("Customers_full_name")
    if search_query:
        requests = Request.objects.filter(Customers_full_name__icontains=search_query)
    ##

    m = []
    k = 0
    for i in requests:
        k+=1
        m.append(k)

    # set up pagination
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    paginator_obj = Paginator(m, 5).get_page(page_number)
    ##

    context = {'requests': requests, 'myFilter': myFilter, 'condition': condition, 'page_obj': page_obj,
               'paginator_obj': paginator_obj}

    return render(request, 'request/request.html', context)


@login_required(login_url='login/')
def autocomplete_cus(request):

    print(request.GET)

    query_original = request.GET.get('term')
    queryset = Request.objects.filter(Customers_full_name__icontains=query_original)
    mylist = []

    mylist += [x.Customers_full_name for x in queryset]

    return JsonResponse(list(set(mylist)), safe=False)


@login_required(login_url='login/')
def autocomplete_lec(request):

    print(request.GET)

    query_original = request.GET.get('term')
    queryset = Request.objects.filter(Lecture_hall__icontains=query_original)
    mylist = []

    mylist += [x.Lecture_hall for x in queryset]

    return JsonResponse(list(set(mylist)), safe=False)


@login_required(login_url='login/')
@permission_required('request.add_request')
def create_request(request):

    req = Request.objects.all()
    work = Type_of_work_list.objects.all()
    perf = Full_name_of_the_performer_list.objects.all()
    condition = Condition_list.objects.all()

    if request.method == 'POST':
        form = Create(request.POST, request.FILES)
        if form.is_valid():
            i = Request(**form.cleaned_data)
            i.save()
            i_pk = str(i.pk)
            # Send message in telegram
            send_telegram_message_async(i_pk)
            ####

            return redirect('/')
    else:
        form = Create()

    context = {'form': form, 'work': work, 'perf': perf, 'condition': condition, 'req': req}

    return render(request, 'create/create.html', context)


def RequestAuth(request):

    requests = Request.objects.all()
    context = {'requests': requests}

    return render(request, 'update/update_view.html', context)


@login_required(login_url='login/')
@permission_required('request.change_request')
def RequestUpdate(request, pk):

    req = Request.objects.get(id=pk)
    form = Create(instance=req)

    if request.method == 'POST':
        form = Create(request.POST, request.FILES, instance=req)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update/update_view.html', context)


class LoginUser(LoginView):

    form_class = AuthenticationForm
    template_name = 'login/login.html'


def logout_user(request):

    logout(request)
    return redirect('login/')


@login_required(login_url='login/')
@permission_required('request.view_request')
def Report(request):

    requests = Request.objects.all()
    work = Type_of_work_list.objects.all()
    perf = Full_name_of_the_performer_list.objects.all()

    myFilter = ReportFilter(request.GET, queryset=requests)
    requests = myFilter.qs
    context = {'requests': requests, 'ReportFilter': myFilter, 'work': work, 'perf': perf}

    return render(request, 'report/report.html', context)


@login_required(login_url='login/')
@permission_required('request.view_request')
def export_excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = ('attachment; filename="Requests"' + str(datetime.datetime.now()) + '.xls')
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Requests')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['ID',
               'Customer',
               'Office',
               'Type of work',
               'Request date',
               'Performer',
               'Condition']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = ReportFilter(request.GET,
                        queryset=Request.objects.all().values_list(
                            'id',
                            'Customers_full_name',
                            'Lecture_hall',
                            'Work__Type_of_work',
                            'Request_date',
                            'Performer__Full_name_of_the_performer',
                            'Condition__Condition')).qs

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):

            if isinstance(row[col_num], datetime.datetime):
                date_time = row[col_num].astimezone(datetime.timezone(datetime.timedelta(hours=7))).strftime('%d/%m/%Y %H:%M')
                ws.write(row_num, col_num, date_time, font_style)

            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response