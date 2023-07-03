from django.contrib import admin
from django.contrib.auth.models import User
from .models import BasicInformation
from .models import ContactPhoneInformation
from .models import ContactEmailInformation


class BasicInformationAdmin(admin.ModelAdmin):
    list_display = ('basic_information_id', 'uid', 'hebrew_first_name', 'hebrew_last_name', 'address', 'father_occupation', 'mother_occupation', 'contact_method', 'user_rating', 'account_status', 'registration_date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'password')


class ContactEmailInformationAdmin(admin.ModelAdmin):
    list_display = ('email_information_id', 'uid', 'email_user', 'email_information')


class ContactPhoneInformationAdmin(admin.ModelAdmin):
    list_display = ('phone_information_id', 'uid', 'phone_user', 'phone_information')


admin.site.register(BasicInformation, BasicInformationAdmin)
admin.site.register(ContactPhoneInformation, ContactPhoneInformationAdmin)
admin.site.register(ContactEmailInformation, ContactEmailInformationAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

