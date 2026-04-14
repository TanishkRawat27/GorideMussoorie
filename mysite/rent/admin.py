from django.contrib import admin
from .models import Booking

# Register your models here.

from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'car_quantity', 'scooty_quantity', 'created_at')

admin.site.register(Booking, BookingAdmin)
