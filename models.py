from django.db import models

import datetime

# Create your models here.
class Reminder(models.Model):
	title = models.CharField(max_length=500)
	date = models.DateField()
	time = models.TimeField()
	note = models.TextField()

	def are_time_date_valid(self):
		current_date = datetime.date.today()
		current_time = datetime.datetime.now().time()

		if (self.date < current_date or (self.date == current_date and self.time < current_time)):
			return False
		return True

	def __str__(self):
		return self.title

