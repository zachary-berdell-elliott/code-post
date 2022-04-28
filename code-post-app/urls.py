from django.urls import path
from . import views
from rest_framework import routers

app_name='code-post-app'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('', views.homepage, name='homepage'),
    path('language/<str>', views.language, name='language'),
    path('snippet/<int:pk>', views.snippet, name=snippet),
    path('user/<int:pk>', views.user_profile, name='user-profile')
]