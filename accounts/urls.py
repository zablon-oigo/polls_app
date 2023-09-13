from django.urls import path
from .views import sign_up,sign_out,sign_in

app_name='accounts'

urlpatterns=[
    path('login/', sign_in, name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/',sign_up, name='register'),
]