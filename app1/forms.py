from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
            model = User                                    #  which model this form to interact with
            fields = ['username', 'email', 'password1', 'password2']  # which fiels are shown in the form and in which order also
