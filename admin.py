from django.contrib import admin

from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['title']}),
	('When to remind', {'fields': ['date', 'time']}),
	('Details', {'fields': ['note']}),
	]
	list_display = ('title', 'date', 'time')
	list_filter = ['date']

# Register your models here.
admin.site.register(Reminder, ReminderAdmin)
