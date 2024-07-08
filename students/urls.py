from django.urls import path
from .views import student_list, student_create, student_update

urlpatterns = [
    path('', views.index, name='index'),
    path('student_list/',views.student_list name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
]
