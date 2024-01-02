from django.contrib import admin
from.models import CustomUser,UserGroup,Event,EventInvitation

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserGroup)
admin.site.register(Event)
admin.site.register(EventInvitation)

