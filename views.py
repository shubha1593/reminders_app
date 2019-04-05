from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
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
	context = {}
	try:
		reminder = Reminder.objects.create(title=data_dict['title'], date=data_dict['date'], time=data_dict['time'], note=data_dict['note'])
		context['message'] = "Reminder added successfully!"
		context['outcome'] = "green"
	except(KeyError, Reminder.DoesNotExist):
		context['message'] = "Error adding reminder. Make sure you filled in all the fields!"
		context['outcome'] = "red"
	return HttpResponseRedirect(reverse('reminders_app:detail', args=(reminder.id,)))

