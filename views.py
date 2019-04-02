from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
#from django.template import loader

from .models import Reminder

# Create your views here.
def index(request):
	latest_reminder_list = Reminder.objects.order_by("-date")[:5]
	#template = loader.get_template("reminders_app/index.html")
	context = {
		'latest_reminder_list': latest_reminder_list,
	}
	return render(request,'reminders_app/index.html' ,context)

def detail(request, reminder_id):
	reminder = get_object_or_404(Reminder, pk=reminder_id)
	return render(request, 'reminders_app/detail.html', {'reminder': reminder})

def add(request):
	return HttpResponse("You're adding a reminder.")
