from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','patient_name','patient_code','complain','gender','address')
# Register your models here.
