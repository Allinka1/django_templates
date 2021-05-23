from django.urls import path
from user.views import user_login, user_logout, profile, register, change_password, interview, suit, no_suit
# from review.views import review

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
    path('interview/', interview, name='interview'),
    path('suit/', suit, name='suit'),
    path('no_suit/', no_suit, name='no_suit'),
]
