from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username',]

class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'text',]

    widgets = {
        'name': forms.TextInput(),
        'email': forms.EmailInput(),
        'text': forms.Textarea(),
    }
        






