from django.db import models

# Create your models here.
class Reminder(models.Model):
	title = models.CharField(max_length=500)
	date = models.DateField()
	time = models.TimeField()
	note = models.TextField()

	def __str__(self):
		return self.title

