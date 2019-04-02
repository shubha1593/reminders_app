from django.urls import path

from . import views

urlpatterns = [
	# /reminders_app
	path('', views.index, name='index'),
	# /reminders_app/7/
	path('<int:reminder_id>/', views.detail, name='detail'),
	# /reminders_app/add/
	path('add/', views.add, name='add'),
]