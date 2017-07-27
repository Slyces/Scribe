from django.shortcuts import render, redirect
from django.views import View
from django.template import RequestContext
from django.db import transaction
from .forms import UserForm, ProfileForm


def home(request):
    return render(request, 'website/home.html')


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        profile_form = ProfileForm(request.POST, prefix='profile')
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('settings:profile')
    else:
        user_form = UserForm(prefix='user')
        profile_form = ProfileForm(prefix='profile')
    return render(request, 'registration/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
    })
