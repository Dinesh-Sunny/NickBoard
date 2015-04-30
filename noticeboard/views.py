from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from noticeboard.models import CreateEvent
from datetime import date, timedelta
import datetime
import requests
import json


# Create your views here.


def events(request):
	if request.session.get("logged_in",False):
		now = datetime.datetime.now()
		tmrw = datetime.date.today() + datetime.timedelta(days=1)
		tmrw = str(tmrw.strftime("%d"))
		events_list_today = CreateEvent.objects.filter(date_time__day=now.strftime("%d"))
		events_list_tomorrow = CreateEvent.objects.filter(date_time__day= tmrw)

		events_list_all = CreateEvent.objects.exclude(date_time__day= tmrw,)
		context = {'events_list_today':events_list_today,'events_list_tomorrow':events_list_tomorrow,
		'events_list_all':events_list_all,"ldapid":request.session["ldapid"]}

        return render(request, 'events.html', context)
 #     return
 # HttpResponse("Not logged_in")
	

def event_detail(request, event_id):
	try:
		event = CreateEvent.objects.get(pk = event_id)
		context = {'event':event}
	except CreateEvent.DoesNotExist:
		raise Http404("Event Does not Exist or Event has been deleted by the User")
	return render(request, 'event_detail.html', context )



def signin(request):
	
	if request.method == 'GET':
		dictionary = {'name':"Sunny"}
		return render(request, 'signin.html',dictionary )
	else:
		ldapid = request.POST.get('ldapId','')
		ldapid_pass = request.POST.get('passwd','')
		url = "http://www.cse.iitb.ac.in/~prithvirajbilla/ldap-api/index.php?user=%s&pass=%s"
		import base64
		encoded = base64.b64encode(ldapid_pass)
		ldapid_pass = encoded

		ldap_content = requests.get(url%(ldapid,ldapid_pass))
		ldap_json = ldap_content.json()
		print ldap_json
		print ldapid_pass
		if ldap_json['bind'] == True:
			request.session["ldapid"] = ldapid
			request.session["logged_in"] = True
			return HttpResponseRedirect('/events')
		else:
			return HttpResponse("not wore")



def logout(request):
	request.session.flush()
	return HttpResponseRedirect("/signin")