from django.urls import path

from users.views import UsersList, UserDetails


urlpatterns = [
    path('', UsersList.as_view(), name="all users"),
    path('<int:pk>/', UserDetails.as_view(), name="user details")
]

import users.signals
