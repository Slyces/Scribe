from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['placeholder'] = 'Enter your {} here'.format(key)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ('facebook_id', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['placeholder'] = 'Enter your {} here'.format(key)
