from django.contrib import admin
from .models import Item
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

admin.site.register(Item, MenuItemAdmin)


#Username (leave blank to use 'rani-pc'): admin
#Email address: admin@admin.com
#password : admin