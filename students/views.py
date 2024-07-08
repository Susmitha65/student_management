
from django.shortcuts import render

def index(request):
    return render(request, 'students/index.html')

def add_student(request):
    # Logic for adding a student (e.g., handling form submission)
    return render(request, 'students/student_form.html')

def student_list(request):
    # Logic for retrieving and displaying the list of students
    # For example, you might fetch data from a database here
    students = [
        {'name': 'John Doe', 'age': 20, 'grade': 'A'},
        {'name': 'Jane Smith', 'age': 22, 'grade': 'B'},
        # Add more student data as needed
    ]
    context = {'students': students}
    return render(request, 'students/student_list.html', context)