from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BasicInformation
from .models import ContactEmailInformation
from .models import ContactPhoneInformation


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Set the username to the email address
        if commit:
            user.save()
        return user


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformation
        fields = ['uid', 'hebrew_first_name', 'hebrew_last_name', 'address', 'father_occupation', 'mother_occupation', 'contact_method', ]


class ContactEmailInformationForm(forms.ModelForm):
    class Meta:
        model = ContactEmailInformation
        fields = ['uid', 'email_user', 'email_information',]


class ContactPhoneInformationForm(forms.ModelForm):
    class Meta:
        model = ContactPhoneInformation
        fields = ['uid', 'phone_user', 'phone_information',]

