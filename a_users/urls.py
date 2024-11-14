from django.urls import path 
from . import views
from django.conf.urls import include
from allauth.account.views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('accounts/', include('allauth.urls')),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('settings/', views.settings, name='settings'),
]
