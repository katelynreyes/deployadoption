from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)
    #email = forms.EmailField(required=True

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]

        def Save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            #user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            if commit:
                user.save()
            return user  


