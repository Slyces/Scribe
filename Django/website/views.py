from django.shortcuts import render, redirect
from django.views import View
from django.template import RequestContext
from django.db import transaction
from .forms import UserForm, ProfileForm


class IndexView(View):
    template_name = 'website/index.html'


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        profile_form = ProfileForm(request.POST, prefix='userprofile')
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            userprofile = profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect('settings:profile')
    else:
        user_form = UserForm(prefix='user')
        profile_form = ProfileForm(prefix='userprofile')
    return render(request, 'registration/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   })
