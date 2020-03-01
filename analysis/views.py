from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.core import serializers
from rest_framework import authentication

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from pprint import pprint
import json

# Create your views here.

def charts(request):
    context = {}
    template_name = 'staff/chat.html'
    return render(request, template_name, context)

def mapdataIframe(request):
    context = {}
    template_name = 'staff/kymao.html'
    return render(request, template_name, context)

def mapdata(request):
    context = {}
    template_name = 'staff/map.html'
    return render(request, template_name, context)

def dashboard(request):
    context = {}
    template_name = 'staff/dashboard.html'
    return render(request, template_name, context)

def coverts_period_date(period):
    period_str = str(period)
    period_month = period_str[-2:]
    period_year = period_str[:-2]
    
    period_date = datetime.date(int(period_year),int(period_month), 1)
    period_date = period_date.strftime('%B')
    

    return period_date
    


def queryApiData(results_dict,indicator_id):
    period_list = []
    ou_list = []
    value_list = []
    indicator_data = results_dict['data'][str(indicator_id)]
    for indicator in indicator_data:
        
        period_list.append(coverts_period_date(indicator['period']))
        ou_list.append(indicator['ou'])
        value_list.append(indicator['value'])


    return period_list, ou_list, value_list

def queryApi(request, *args, **kwargs):

    context = {}
    # indicator_api_url = 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=18&level=2'
    indicator_api_url = 'http://41.89.94.105/dsl/api/indicators/'
    api_url= 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=23409&level=2'
    organisation_unit_api_url = 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=18&level=2'

    headers = {"Accept": "application/json"}
    
    response = requests.get(api_url, headers=headers)
    indicator_api_resposnse = requests.get(indicator_api_url, headers=headers)
    organisation_unit_api_response = requests.get(organisation_unit_api_url, headers=headers)
    
    response_data = response.json() #Full retrieved data

    #Full retrieved indicator data
    indicator_context = []

    organisation_unit_context = []
    organisation_unit_data = organisation_unit_api_response.json()
    context['indicator_context'] = indicator_api_resposnse.json()
    context['organisation_unit_context'] = organisation_unit_data['result']['dictionary']['orgunits']
    
        
    pprint(context['organisation_unit_context'])
    # getting the labels
    county_list = []
    # getting the data
    county_data_list = []
    #
    results_dict=response_data['result']
    orgunit_list = results_dict['dictionary']['orgunits']
    pprint(results_dict)

    context['county_name_list']=[]
    context['county_name_list_id']=[]
    context['period_list'],context['ou_list'] ,context['value_list']  = queryApiData(results_dict,21030) #change query


    for orgunit in orgunit_list:
        context['county_name_list'].append(orgunit['name'])
        context['county_name_list_id'].append(orgunit['id'])

    return JsonResponse(context)

def customSearchView(request):
    context = {}
    if request.method == 'GET':
        indicator = int(request.GET.get('indicatorparam'))
        pe = request.GET.get('pe')
        ouid = request.GET.get('ouid')

        indicator_api_url = f'http://41.89.94.105/dsl/api/indicators/'
        api_url= f'http://41.89.94.105/dsl/api/indicators/{indicator}?pe={pe}&ouid={ouid}&level=2'
        organisation_unit_api_url = f'http://41.89.94.105/dsl/api/indicators/{indicator}?pe={pe}&ouid=18&level=2'

        headers = {"Accept": "application/json"}
    
        response = requests.get(api_url, headers=headers)
        indicator_api_resposnse = requests.get(indicator_api_url, headers=headers)
        organisation_unit_api_response = requests.get(organisation_unit_api_url, headers=headers)
        
        response_data = response.json() #Full retrieved data

        #Full retrieved indicator data
        indicator_context = []

        organisation_unit_context = []
        organisation_unit_data = organisation_unit_api_response.json()
        context['indicator_context'] = indicator_api_resposnse.json()
        context['organisation_unit_context'] = organisation_unit_data['result']['dictionary']['orgunits']
        
            
        pprint(context['organisation_unit_context'])
        # getting the labels
        county_list = []
        # getting the data
        county_data_list = []
        #
        results_dict=response_data['result']
        orgunit_list = results_dict['dictionary']['orgunits']
        pprint(results_dict)

        context['county_name_list']=[]
        context['county_name_list_id']=[]
        context['period_list'],context['ou_list'] ,context['value_list']  = queryApiData(results_dict, int(indicator)) #change query


        for orgunit in orgunit_list:
            context['county_name_list'].append(orgunit['name'])
            context['county_name_list_id'].append(orgunit['id'])
    
    
    template_name = 'staff/customsearch.html'

    return render(request, template_name, context)


def customAjaxSearchView(request):
    context = {}
    if request.method == 'GET':
        indicator = int(request.GET.get('indicatorparam'))
        pe = request.GET.get('pe')
        ouid = request.GET.get('ouid')

        indicator_api_url = f'http://41.89.94.105/dsl/api/indicators/'
        api_url= f'http://41.89.94.105/dsl/api/indicators/{indicator}?pe={pe}&ouid={ouid}&level=2'
        organisation_unit_api_url = f'http://41.89.94.105/dsl/api/indicators/{indicator}?pe={pe}&ouid=18&level=2'

        headers = {"Accept": "application/json"}
    
        response = requests.get(api_url, headers=headers)
        indicator_api_resposnse = requests.get(indicator_api_url, headers=headers)
        organisation_unit_api_response = requests.get(organisation_unit_api_url, headers=headers)
        
        response_data = response.json() #Full retrieved data

        #Full retrieved indicator data
        indicator_context = []

        organisation_unit_context = []
        organisation_unit_data = organisation_unit_api_response.json()
        context['indicator_context'] = indicator_api_resposnse.json()
        context['organisation_unit_context'] = organisation_unit_data['result']['dictionary']['orgunits']
        
            
        pprint(context['organisation_unit_context'])
        # getting the labels
        county_list = []
        # getting the data
        county_data_list = []
        #
        results_dict=response_data['result']
        orgunit_list = results_dict['dictionary']['orgunits']
        pprint(results_dict)

        context['county_name_list']=[]
        context['county_name_list_id']=[]
        context['period_list'],context['ou_list'] ,context['value_list']  = queryApiData(results_dict, int(indicator)) #change query


        for orgunit in orgunit_list:
            context['county_name_list'].append(orgunit['name'])
            context['county_name_list_id'].append(orgunit['id'])
    
    
    # template_name = 'staff/customsearch.html'

    # return render(request, template_name, context)
    
    return JsonResponse(context)