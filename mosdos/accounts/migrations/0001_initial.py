# Generated by Django 4.2.2 on 2023-07-02 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('basic_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('hebrew_first_name', models.CharField(max_length=255)),
                ('hebrew_last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('father_occupation', models.CharField(max_length=255)),
                ('mother_occupation', models.CharField(max_length=255)),
                ('contact_method', models.CharField(max_length=255)),
                ('user_rating', models.CharField(default='white', max_length=255)),
                ('account_status', models.CharField(default='active', max_length=255)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]