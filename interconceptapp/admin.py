from django.contrib import admin
from .models import Contact, Management

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'message', 'contact_date')
    list_per_page = 25

class ManagementAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'linkedn_url')
    list_per_page = 23


    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Management, ManagementAdmin)
