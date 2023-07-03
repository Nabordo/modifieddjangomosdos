from django.db import models
from django.contrib.auth.models import User


class UserVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)


class BasicInformation(models.Model):
    basic_information_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    hebrew_first_name = models.CharField(max_length=255)
    hebrew_last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    contact_method = models.CharField(max_length=255)
    user_rating = models.CharField(max_length=255, default='white')
    account_status = models.CharField(max_length=255, default='active')
    registration_date = models.DateTimeField(auto_now_add=True)


class ContactEmailInformation(models.Model):
    email_information_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    email_user = models.CharField(max_length=255)
    email_information = models.CharField(max_length=255)


class ContactPhoneInformation(models.Model):
    phone_information_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    phone_user = models.CharField(max_length=255)
    phone_information = models.CharField(max_length=255)

