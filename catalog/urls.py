from django.contrib import admin
from django.urls import path, include
from . import views
from .views import adoption_application

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # the main page
    path('pet_list/', views.PetListView.as_view(), name='pet_list'),  # Pet list page
    path('pet_detail/<int:pk>', views.PetDetailView.as_view(), name='pet_detail'),
    path('volunteer/', views.volunteer, name='volunteer'),  # Volunteer information page
    path('adoption/', adoption_application, name='adoption_application'),#application page
    path('application_submitted/', views.application_submitted, name='application_submitted'), # successful submission

]
