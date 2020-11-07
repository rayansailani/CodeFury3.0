from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "accounts"
urlpatterns = [
    path('register/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
]
