from django.contrib import admin
from noticeboard.models import CreateEvent
# Register your models here.

class CreateEventAdmin(admin.ModelAdmin):
	search_fields = ['event_name']
	fields = ['event_name','venue','date_time','seats','event_description',
	'event_instructions','option_website_link','option_contact_info',]
	
admin.site.register(CreateEvent,CreateEventAdmin)
