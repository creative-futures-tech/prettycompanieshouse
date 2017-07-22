from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^companies/search/$', views.get_companies_house_info, name='companies_house_info'),
    url(r'^download/$', views.download_pdf, name='download_pdf'),
]
