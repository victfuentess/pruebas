from django.urls import path
from django.conf.urls import include

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('users/', views.ListUser.as_view(), name="users"),
    path('users/<int:id>', views.ListUser.as_view(), name="users"),
    path('token-auth/', obtain_auth_token, name='token_auth'),
]

