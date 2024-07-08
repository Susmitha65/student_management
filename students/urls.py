from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student/', views.add_student, name='add_student'),
    path('student-list/', views.student_list, name='student_list'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
]
