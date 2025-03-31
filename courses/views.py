from django.shortcuts import render, get_object_or_404
from .models import Course, Student, Enrollment

# Course List View --------------------------------------------------------------/
def course_list(request):
    """
    Display a list of all available courses.
    
    Returns:
        A rendered template showing all courses in a table format, with each row
        containing the course code, name, credits, semester offered, and a brief
        description. Courses are ordered by their code.
    """
    courses = Course.objects.all()

    return render(request, 'courses/course_list.html', { 'courses': courses })

# Course Detail View ------------------------------------------------------------
def course_detail(request, pk):
    """
    Display detailed information about a specific course and its enrolled students.
    
    Args:
        pk: The primary key of the course to display.
        
    Returns:
        A rendered template showing:
        - Course details (code, name, credits, semester, description)
        - List of prerequisites (if any)
        - List of currently enrolled students with their grades
        
    Raises:
        Http404: If the course with the specified pk doesn't exist.
    """
    course = get_object_or_404(Course, pk=pk)
    enrollments = Enrollment.objects.filter(course=course
                                            
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'enrollments': enrollments
    })

# Student List View -------------------------------------------------------------
def student_list(request):
    """
    Display a list of all registered students.
    
    Returns:
        A rendered template showing all students in a table format, with each row
        containing the student's name, email, major, and year level.
        Students are ordered alphabetically by name.
    """
    students = Student.objects.all()

    return render(request, 'courses/student_list.html', { 'students': students })

# Student Detail View ------------------------------------------------------------
def student_detail(request, pk):
    """
    Display detailed information about a specific student and their course enrollments.
    
    Args:
        pk: The primary key of the student to display.
        
    Returns:
        A rendered template showing:
        - Student information (name, email, major, year)
        - List of all course enrollments with grades
        
    Raises:
        Http404: If the student with the specified pk doesn't exist.
    """
    student = get_object_or_404(Student, pk=pk)
    enrollments = Enrollment.objects.filter(student=student)

    return render(request, 'courses/student_detail.html', {
        'student': student,
        'enrollments': enrollments
    })

# Enrollment List View ----------------------------------------------------------
def enrollment_list(request):
    """
    Display a list of all course enrollments, ordered alphabetically by student name.
    
    Returns:
        A rendered template showing all enrollments in a table format, with each row
        containing the student name, course details, semester, and grade status.
        Students are sorted alphabetically by name.
    """
    enrollments = Enrollment.objects.all().order_by('student__name')
    return render(request, 'courses/enrollment_list.html', { 'enrollments': enrollments })
