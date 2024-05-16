from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            customer = authenticate(request,
                                    username=cleaned_data['username'],
                                    password=cleaned_data['password'])
            if customer is not None:
                if customer.is_active:
                    login(request, customer)
                    return HttpResponse('Authentication Valid')

                else:
                    return HttpResponse('Authentication Invalid')
            else:
                return HttpResponse('Invalid Login')

        else:
            form = LoginForm()
        return render(request, 'registration/logged_out.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save() # Added
            customer.save()
            messages.success(request, "Registration Successful.")
            # return redirect('/')
            return render(request, template_name='registration/register_done.html')
        messages.error(request, "Registration Unsuccessful.")
    form = RegisterForm()
    return render(request, "register.html", {"form": form})
    # return render(request, template_name='registration/register_done.html', context={'register_form': form})

