from django import forms



class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.Form):
    facebook_id = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=10, min_length=10)
