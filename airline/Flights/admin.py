from django.contrib import admin
from .models import Flight , airport, Passenger
# Register your models here.

admin.site.register(Flight)
admin.site.register(airport)
admin.site.register(Passenger)