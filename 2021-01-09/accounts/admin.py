from django.contrib import admin
from .models import Profile
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'person_name', 'age', 'email', 'created_at', 'updated_at']
    list_filter = ('user__username', 'person_name', 'email', 'age',
                   ('created_at', DateTimeRangeFilter),
                   ('updated_at', DateTimeRangeFilter),
                   ('birthday', DateRangeFilter),
                   'phone_number', 'home_address')
    search_fields = ['user__username', 'person_name', 'email', 'age', 'created_at', 'updated_at',
                     'phone_number', 'home_address', 'birthday']