from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student),
    path('faculty/', views.faculty),
    path('course/', views.course),
]