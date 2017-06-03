BASE_URL= "https://api.companieshouse.gov.uk/"
COMPANIES_HOUSE_API_KEY='Fagm7rhqnin6p9r_PFoYVG73YWUaG7gMd-4QufVI'

def _url(trailing):
    return "%s%s" % (BASE_URL, trailing)