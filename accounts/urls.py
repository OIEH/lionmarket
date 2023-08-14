from django.urls import path, include
from . import views
from .views import signup_view,login_view,check_view,logout_view
from rest_framework import urls

app_name = 'accounts'

urlpatterns = [
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]
