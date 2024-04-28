from django import forms

from django import forms
from .models import AdoptionApplication


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['full_name', 'email', 'phone_number', 'address', 'why_you_want_to_adopt', 'name_of_pet']
        widgets = {
            'why_you_want_to_adopt': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
    address = forms.CharField(required=False)  # Ensure address is not required
