from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from noticeboard.models import CreateEvent

# Create your views here.

def events(request):
	events_list = CreateEvent.objects.order_by('-date_time')
	context = {'events_list':events_list,}

	return render(request, 'events.html', context)
	

def event_detail(request, event_id):
	try:
		event = CreateEvent.objects.get(pk = event_id)
		context = {'event':event}
	except CreateEvent.DoesNotExist:
		raise Http404("Event Does not Exist or Event has been deleted by the User")
	return render(request, 'event_detail.html', context )