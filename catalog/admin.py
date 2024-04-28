from django.contrib import admin
from django.utils import timezone
from datetime import timedelta, date
from .models import Pet, PetInstance, Appointment, AdoptionApplication


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_date', 'client_name', 'appointment_type')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        now = timezone.now()
        upcoming = now + timedelta(days=30)
        return qs.filter(appointment_date__range=(now, upcoming))


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'get_age', 'available_for_adoption')
    list_filter = ('available_for_adoption', 'breed')
    search_fields = ('name', 'breed')

    def get_age(self, obj):
        if obj.date_of_birth:
            return date.today().year - obj.date_of_birth.year
        else:
            return 'Unknown'

    get_age.short_description = 'Age'


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('user','full_name', 'email', 'phone_number', 'address', 'name_of_pet')
    list_filter = ('name_of_pet',)
    search_fields = ('full_name', 'email', 'address', 'name_of_pet')


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PetInstance)
