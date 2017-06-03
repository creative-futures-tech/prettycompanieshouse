from django.shortcuts import render
from companies_house import search
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'prettycompanieshouse_app/index.html', {})


def get_companies_house_info(request):
    tmp_company_name =  request.POST.get('search')
    companies_found = search.search_by_name(tmp_company_name)
    return JsonResponse({'companies': companies_found})