from django.contrib import admin
from .models import User, Event, VolunteerRegistration, EnvironmentalResource, ImpactReport, Recognition

admin.site.register(User),
admin.site.register(EnvironmentalResource),
admin.site.register(VolunteerRegistration),
admin.site.register(Event),
admin.site.register(ImpactReport),
admin.site.register(Recognition),   