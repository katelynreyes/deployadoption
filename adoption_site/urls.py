from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),

    # forgot password - reset
    path('password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),

    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

    # IMPORTANT – THE URL BELOW MUST BE AFTER THE PASSWORD RESET CUSTOM FORM
    # ABOVE if included- was in front of the reset password
    # bringing up the django version first
    # path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
