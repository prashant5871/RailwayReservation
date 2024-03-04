from django.contrib import admin
from .models import *;
# Register your models here.

admin.site.register(Register)
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Passenger)
admin.site.register(Ticket)

