from django.urls import path
from allauth.account.views import confirm_email

from .views import SignupPageView

urlpatterns = [
    path('accounts/confirm-email/<str:key>/', confirm_email, name='account_confirmation_email'),
    path('signup/', SignupPageView.as_view(), name='signup')

]