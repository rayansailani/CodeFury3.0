from django.urls import path, include
from . import views

app_name = 'create'
urlpatterns = [
    path("employee/", views.register, name="register"),
    path('company/', views.regCompany, name="regcom"),
]
