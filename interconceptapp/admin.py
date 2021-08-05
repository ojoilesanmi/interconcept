from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'message', 'contact_date')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
