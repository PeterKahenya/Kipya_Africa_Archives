from django.contrib import admin
from .models import Attendee2020

class Attendee2020Admin(admin.ModelAdmin):
    list_display= ('title', 'first_name', 'last_name', 'organization','job_title','role','gak_no','country','email','phone','mpesa_code','mpesa_name','mpesa_amount','created','last_modified')

admin.site.register(Attendee2020,Attendee2020Admin)


