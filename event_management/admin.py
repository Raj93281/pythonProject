from django.contrib import admin
from.models import CustomUser,UserGroup,Event,EventInvitation,Product,Cart,CartItem

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserGroup)
admin.site.register(Event)
admin.site.register(EventInvitation)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

