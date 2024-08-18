from django.urls import path
from database import views

urlpatterns = [
    path('students-list/', views.StudentsListView.as_view(), name='students-list'),
    path('teachers-list/', views.teacher_list, name='teachers-list'),
    path('student-detail/<int:pk>/', views.student_details, name='student-detail')
]