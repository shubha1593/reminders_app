from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
import datetime
#from django.template import loader

from .models import Reminder

class IndexView(generic.ListView):
	template_name = 'reminders_app/index.html'
	context_object_name = 'latest_reminder_list'

	def get_queryset(self):
		""" Return the last five reminders. """
		return Reminder.objects.order_by("-date")[:5]

class DetailView(generic.DetailView):
	model = Reminder
	template_name = 'reminders_app/detail.html'
		
def detail(request, reminder_id):
	reminder = get_object_or_404(Reminder, pk=reminder_id)
	return render(request, 'reminders_app/detail.html', {'reminder': reminder})

def add(request):
	return render(request, 'reminders_app/add.html')

def insert(request):
	data_dict = request.POST
	print (data_dict)
	date = datetime.datetime.strptime(data_dict['date'], "%Y-%m-%d").date()
	time = datetime.datetime.strptime(data_dict['time'], "%H:%M").time()
	try:
		reminder = Reminder(title=data_dict['title'], date=date, time=time, note=data_dict['note'])
	except (KeyError, Reminder.DoesNotExist):
		return render(request, 'reminders_app/add.html', {'error_message': "You haven't filled in all the fields."})
	else:
		if reminder.are_time_date_valid():
			reminder.save()
			return HttpResponseRedirect(reverse('reminders_app:detail', args=(reminder.id,)))
		else:
			return render(request, 'reminders_app/add.html', {'error_message': "Can't remind you for an event in the past!"})
