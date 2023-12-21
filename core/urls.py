from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import contact_view
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact_view'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
