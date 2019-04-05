from django.urls import path

from . import views

app_name = 'reminders_app'

urlpatterns = [
	# /reminders_app
	path('', views.IndexView.as_view(), name='index'),
	# /reminders_app/7/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# /reminders_app/add/
	path('add/', views.add, name='add'),
	# /reminders_app/insert/
	path('insert/', views.insert, name='insert'),
]