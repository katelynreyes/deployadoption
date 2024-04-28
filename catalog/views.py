from django.shortcuts import render
from django.views import generic
from .models import Pet
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet, PetInstance
from django.shortcuts import render, redirect
from .forms import AdoptionForm
from catalog.forms import AdoptionForm
from django.contrib.auth.decorators import login_required



def index(request):
    """View function for home page of site."""
    context = {
        'test': 'Testing'
    }

    return render(request, 'catalog/index.html', context=context)


def volunteer_view(request):
    return render(request, 'catalog/volunteer.html')


def volunteer(request):
    return render(request, 'catalog/volunteer.html')


class PetDetailView(generic.DetailView):
    model = Pet


class PetListView(generic.ListView):
    model = Pet


from django.contrib.auth.decorators import login_required

@login_required
def adoption_application(request):
    if request.method == 'POST':
        # If the form is submitted via POST, instantiate the AdoptionForm with the submitted data
        form = AdoptionForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the form data to the database
            # Set the user of the adoption application to the current logged-in user
            if request.user.is_authenticated:
                form.instance.user = request.user
            form.save()
            # Redirect to a success page
            return redirect('application_submitted')
    else:
        # If the request method is not POST (e.g., GET), instantiate an empty AdoptionForm
        form = AdoptionForm()

    # Pass the form instance to the template context
    return render(request, 'adoption_form.html', {'form': form})

# defines the view for the success page
def application_submitted(request):
    return render(request, 'application_submitted.html')
