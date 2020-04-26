from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Meeting
from .models import MeetingMinutes
from .models import Resource
from .models import Event

admin.site.register(Meeting)
admin.site.unregister(MeetingMinutes)
admin.site.unregister(Resource)
admin.site.unregister(Event)

admin.site.site_header = "Python Club"



