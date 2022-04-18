from django.contrib.auth.forms import *
from django import forms


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ("username", "email", 'phone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
