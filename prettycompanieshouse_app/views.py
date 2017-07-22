from django.shortcuts import render
from companies_house import search
from django.http import JsonResponse, HttpResponse
import pdfkit

pdf_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
# Create your views here.
def index(request):
    return render(request, 'prettycompanieshouse_app/index.html', {})


def get_companies_house_info(request):
    tmp_company_name =  request.POST.get('search')
    companies_found = search.search_by_name(tmp_company_name)
    request.session['companies'] = companies_found
    return JsonResponse({'companies': companies_found})


def print_info_from_company(request, company_nr):
    pass


def download_pdf(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    pdf = pdfkit.from_url('http://google.com', False, configuration=pdf_config)
    response.write(pdf)
    return response