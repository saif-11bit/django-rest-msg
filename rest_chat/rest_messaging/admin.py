from django.contrib import admin
from .models import Participant, Thread, Participation, Message, NotificationCheck


admin.site.register(Participant)
admin.site.register(Thread)
admin.site.register(Participation)
admin.site.register(Message)
admin.site.register(NotificationCheck)

