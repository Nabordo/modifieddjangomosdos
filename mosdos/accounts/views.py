from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import UserVerification
from django.contrib.auth.decorators import login_required
from .models import BasicInformation, ContactPhoneInformation
from .forms import BasicInformationForm
from .forms import ContactEmailInformationForm
from django.shortcuts import render, redirect
from .forms import ContactPhoneInformationForm


def profile_view(request):
    user_id = request.user.id
    basic_info, created = BasicInformation.objects.get_or_create(uid=user_id)

    if request.method == 'POST':
        form = BasicInformationForm(request.POST, instance=basic_info)
        email_form_father = ContactEmailInformationForm(request.POST, prefix='email_father')
        email_form_mother = ContactEmailInformationForm(request.POST, prefix='email_mother')
        phone_form = ContactPhoneInformationForm(request.POST, prefix='phone')
        phone_form_father = ContactPhoneInformationForm(request.POST, prefix='phone_father')
        phone_form_mother = ContactPhoneInformationForm(request.POST, prefix='phone_mother')

        if form.is_valid():
            form.save()

        if email_form_father.is_valid():
            email_info_father = email_form_father.save(commit=False)
            email_info_father.uid = user_id
            email_info_father.save()

        if email_form_mother.is_valid():
            email_info_mother = email_form_mother.save(commit=False)
            email_info_mother.uid = user_id
            email_info_mother.save()

        if phone_form.is_valid():
            phone_info = phone_form.save(commit=False)
            phone_info.save()

        if phone_form_father.is_valid():
            phone_info_father = phone_form_father.save(commit=False)
            phone_info_father.save()

        if phone_form_mother.is_valid():
            phone_info_mother = phone_form_mother.save(commit=False)
            phone_info_mother.save()

        return redirect('profile')
    else:
        form = BasicInformationForm(instance=basic_info)
        email_form_father = ContactEmailInformationForm(prefix='email_father')
        email_form_mother = ContactEmailInformationForm(prefix='email_mother')
        phone_form = ContactPhoneInformationForm(prefix='phone')
        phone_father = ContactPhoneInformationForm(prefix='phone_father')
        phone_mother = ContactPhoneInformationForm(prefix='phone_mother')

    return render(request, 'profiles/home.html', {'basic_info': basic_info, 'form': form, 'email_form_father': email_form_father, 'email_form_mother': email_form_mother, 'phone_form': phone_form, 'phone_father': phone_father, 'phone_mother': phone_mother})







@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the dashboard page
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')


def verify_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        verification = UserVerification.objects.get(user=user, token=token)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            verification.delete()
            return render(request, 'registration/account_verified.html')

        # Token is invalid or expired
        return render(request, 'registration/verification_invalid.html')

    except (UserVerification.DoesNotExist, User.DoesNotExist, ValueError, OverflowError):
        # Invalid user or verification entry not found
        return render(request, 'registration/verification_invalid.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until email verification
            user.save()

            # Generate verification token
            token = default_token_generator.make_token(user)

            # Create UserVerification entry
            verification = UserVerification.objects.create(user=user, token=token)

            # Send verification email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message_text = render_to_string('registration/verification_email.txt', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            })
            message_html = render_to_string('registration/verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            })
            email = EmailMultiAlternatives(mail_subject, message_text, to=[user.email])
            email.attach_alternative(message_html, "text/html")
            email.send()

            # Redirect to success page or show a message
            return redirect('registration_success')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def registration_success(request):
    return render(request, 'registration/registration_success.html')
