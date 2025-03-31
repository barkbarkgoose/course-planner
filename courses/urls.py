"""URLs for the course planning application."""

from django.urls import path
from courses import views

# pylint: disable=invalid-name
app_name = 'courses'

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
]
 