from django.urls import path
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('profile/', ProfileView.as_view()),
]
