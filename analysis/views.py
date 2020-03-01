from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.core import serializers
from rest_framework import authentication

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

# Create your views here.

def charts(request):
    context = {}
    template_name = 'staff/chat.html'
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
    print('period_month', period_month)
    print('period_year', period_year)
    # period_date_str = period + "01"
    period_date = datetime.date(int(period_year),int(period_month), 1)
    period_date = period_date.strftime('%B')
    print(period_date)
    # year = array.array(i, period_date)

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
    # api_url = 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=18&level=2'
    api_url= 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=23409&level=2'

    headers = {"Accept": "application/json"}
    
    response = requests.get(api_url, headers=headers)
    
    response_data = response.json() #Full retrieved data

    # getting the labels
    county_list = []
    # getting the data
    county_data_list = []
    #
    results_dict=response_data['result']
    orgunit_list = results_dict['dictionary']['orgunits']

    context['county_name_list']=[]
    context['county_name_list_id']=[]
    context['period_list'],context['ou_list'] ,context['value_list']  = queryApiData(results_dict,21030) #change query
    
    # print(context['period_list'])
    # print(context['ou_list'])
    # print(context['value_list'])

    for orgunit in orgunit_list:
        context['county_name_list'].append(orgunit['name'])
        context['county_name_list_id'].append(orgunit['id'])

    # print(context)
    

    # for result_key in results_dict:
    #     for dictionary_key in results_dict[result_key]:
    #        context['dictionary']=results_dict[result_key]['dictionary']
    #        context['data']=results_dict[result_key]['data']
    
    
    # pprint(response.json)

    return JsonResponse(context)


# class ChartData(APIView):
#     authentication_classes = []

#     def queryApiData(self, results_dict,indicator_id):
#         period_list = []
#         ou_list = []
#         value_list = []
#         indicator_data = results_dict['data'][str(indicator_id)]
#         for indicator in indicator_data:
#             period_list.append(indicator['period'])
#             ou_list.append(indicator['ou'])
#             value_list.append(indicator['value'])


#         return period_list, ou_list, value_list

#     def queryApi(self, request, *args, **kwargs):

#         context = {}
#         api_url = 'http://41.89.94.105/dsl/api/indicators/21030?pe=2019&ouid=18&level=2'

#         headers = {"Accept": "application/json"}
        
#         response = requests.get(api_url, headers=headers)
        
#         response_data = response.json() #Full retrieved data

#         # getting the labels
#         county_list = []
#         # getting the data
#         county_data_list = []
#         #
#         results_dict=response_data['result']
#         orgunit_list = results_dict['dictionary']['orgunits']

#         context['county_name_list']=[]
#         context['county_name_list_id']=[]
#         context['period_list'],context['ou_list'] ,context['value_list']  = queryApiData(results_dict,21030) #change query
        
#         # print(context['period_list'])
#         # print(context['ou_list'])
#         # print(context['value_list'])

#         for orgunit in orgunit_list:
#             context['county_name_list'].append(orgunit['name'])
#             context['county_name_list_id'].append(orgunit['id'])


#         return Response()


