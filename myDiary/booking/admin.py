from django.contrib import admin
from . models import Booking, MeetingPlace


class BookingAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'meeting_date', 'start_time', 'end_time')
    
    search_fields = ('title', 'meeting_date', 'start_time', 'end_time')

admin.site.register(Booking, BookingAdmin)
admin.site.register(MeetingPlace)