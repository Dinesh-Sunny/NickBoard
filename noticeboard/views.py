from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from noticeboard.models import CreateEvent
from datetime import date, timedelta
import datetime

# Create your views here.


def events(request):
	now = datetime.datetime.now()
	tmrw = datetime.date.today() + datetime.timedelta(days=1)
	tmrw = str(tmrw.strftime("%d"))
	events_list_today = CreateEvent.objects.filter(date_time__day=now.strftime("%d"))
	events_list_tomorrow = CreateEvent.objects.filter(date_time__day= tmrw)

	events_list_all = CreateEvent.objects.exclude(date_time__day= tmrw,)
	context = {'events_list_today':events_list_today,'events_list_tomorrow':events_list_tomorrow,'events_list_all':events_list_all,}

	return render(request, 'events.html', context)
	

def event_detail(request, event_id):
	try:
		event = CreateEvent.objects.get(pk = event_id)
		context = {'event':event}
	except CreateEvent.DoesNotExist:
		raise Http404("Event Does not Exist or Event has been deleted by the User")
	return render(request, 'event_detail.html', context )