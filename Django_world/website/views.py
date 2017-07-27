from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.db import transaction
from .models import *
from .forms import UserForm, ProfileForm


def home(request):
    return render(request, 'website/home.html')


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        profile_form = ProfileForm(request.POST, prefix='profile')
        if user_form.is_valid() and profile_form.is_valid():
            user = User.objects.create_user(
                user_form.cleaned_data['username'],
                password= user_form.cleaned_data['password'],
                email= user_form.cleaned_data['email'],
                first_name= user_form.cleaned_data['first_name'],
                last_name= user_form.cleaned_data['last_name'],
            )
            profile = Profile.objects.create(
                user= user,
                facebook_id= profile_form.cleaned_data['facebook_id'],
                phone_number= profile_form.cleaned_data['phone_number'],
            )
            user.save()
            profile.save()
            return redirect(reverse('website:home'))
    else:
        user_form = UserForm(prefix='user')
        profile_form = ProfileForm(prefix='profile')
    return render(request, 'registration/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
    })
