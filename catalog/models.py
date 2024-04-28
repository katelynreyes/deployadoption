from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique pet instances


class Pet(models.Model):
    """Model representing a pet."""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    history = models.TextField(max_length=500, help_text='Enter a brief description of the pet')
    breed = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    pet_image = models.ImageField(upload_to='images/', null=True, blank=True)
    available_for_adoption = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this pet."""
        return reverse('pet_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)."""
        return self.name


class PetInstance(models.Model):
    """Model representing a specific pet that can have an appointment created to visit."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this pet")
    pet = models.ForeignKey('Pet', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.pet.name})'


class Appointment(models.Model):
    """Model representing an appointment."""
    client_name = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.appointment_date} - {self.client_name}'


class AdoptionApplication(models.Model):
    """Model representing an adoption application."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    why_you_want_to_adopt = models.CharField(max_length=500)
    name_of_pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.full_name} - {self.name_of_pet}'
