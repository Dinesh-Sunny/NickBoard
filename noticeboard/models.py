from django.db import models

# Create your models here.

class CreateEvent(models.Model):
	event_name = models.CharField(max_length=200)
	venue = models.CharField(max_length=20)
	date_time = models.DateField()
	seats = models.IntegerField(default = 200)
	event_description = models.CharField(max_length = 1000)
	event_instructions = models.CharField(max_length = 500)
	option_website_link = models.CharField(max_length = 100)
	option_contact_info =  models.CharField(max_length = 100)

	def __str__:
		return event_name + " " +venue+ " "+ seats