
from .config import COMPANIES_HOUSE_API_KEY, _url
import requests

def search_by_name(name, items_per_page = 5):
    """

    :param name: company name to search
    :param items_per_page: results to return on a single call
    :return: list of company name, number and address found
    """
    res = requests.get(_url('search/companies?q=%s&items_per_page=5' % name), auth=(COMPANIES_HOUSE_API_KEY, ''))
    body = res.json()
    return [{'title': company['title'],
             'number': company['company_number'],
             'address': company['address_snippet']} for company in  body['items']]



def search_by_number(company_number):
    pass


