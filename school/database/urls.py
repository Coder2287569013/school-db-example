from django.urls import path
from database import views

urlpatterns = [
    path('students-list/', views.StudentsListView.as_view(), name='students-list'),
]