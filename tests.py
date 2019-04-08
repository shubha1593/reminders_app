from django.test import TestCase, Client
from django.urls import reverse

import datetime

from .models import Reminder

client = Client()

def create_reminder(title, date, time, note):
	return Reminder.objects.create(title=title, date=date, time=time, note=note)

# Create your tests here.
class ReminderModelTests(TestCase):

	def test_are_time_date_valid_with_past_reminder(self):
		"""
		are_time_date_valid() returns False for reminders set for past time. 
		"""
		reminder_date = datetime.date.today() - datetime.timedelta(days=2)
		reminder_time = (datetime.datetime.now() - datetime.timedelta(hours=2)).time()

		reminder_1 = Reminder(title="test reminder 1", date=reminder_date, time=datetime.datetime.now().time(), note="note for test reminder 1")
		reminder_2 = Reminder(title="test reminder 2", date=datetime.date.today(), time=reminder_time, note="note for test reminder 2")
		self.assertEqual(reminder_1.are_time_date_valid(), False)
		self.assertEqual(reminder_2.are_time_date_valid(), False)

class ReminderIndexViewTests(TestCase):
	"""
	If no reminders exists, an appropriate message is displayed.
	"""
	def test_no_reminder(self):
		response = self.client.get(reverse('reminders_app:index'))
		self.assertContains(response, "No reminders!")

	def test_past_reminder(self):
		"""
		Reminder for a past time will show an error on the add page
		"""
		reminder_date = datetime.date.today() - datetime.timedelta(days=2)
		reminder_time = (datetime.datetime.now() - datetime.timedelta(hours=2)).time()
		create_reminder("test with past time", reminder_date, reminder_time, "Trying to create a reminder with a past date/time.")
		response = self.client.get(reverse('reminders_app:index'))
		self.assertQuerysetEqual(response.context['latest_reminder_list'], [])

class ReminderDetailViewTests(TestCase):

	def test_past_reminder(self):
		"""
		The detail view of a reminder with a past date/time returns a 404 not found.
		"""
		reminder_date = datetime.date.today() - datetime.timedelta(days=2)
		reminder_time = (datetime.datetime.now() - datetime.timedelta(hours=2)).time()
		past_reminder = create_reminder("test with past time", reminder_date, reminder_time, "Trying to create a reminder with a past date/time.")
		url = reverse('reminders_app:detail', args=(past_reminder.id))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)
