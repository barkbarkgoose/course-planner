from django.db import models


class Course(models.Model):
    """
    Represents a course in the academic system.
    
    Attributes:
        name: The full name of the course
        code: Unique course code (e.g., CS101)
        description: Detailed course description
        credits: Number of credit hours
        prerequisites: Related courses that must be completed first
        semester_offered: When the course is typically offered
    """
    SEMESTER_CHOICES = [
        ('FALL', 'Fall'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
    ]
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    credits = models.IntegerField()
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    semester_offered = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        ordering = ['code']

class Student(models.Model):
    """
    Represents a student enrolled in the academic system.
    
    Attributes:
        name: Student's full name
        email: Unique email address
        major: Student's declared major
        year: Current academic year level
    """
    YEAR_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)

    def __str__(self):
        # pylint: disable=no-member
        return f"{ self.name } ({ self.get_year_display() })"
        
    class Meta:
        ordering = ['name']

class Enrollment(models.Model):
    """
    Represents a student's enrollment in a specific course.
    
    Attributes:
        student: The enrolled student
        course: The course being taken
        semester: The semester of enrollment
        grade: The grade received (if completed)
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=6, choices=Course.SEMESTER_CHOICES)
    grade = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        unique_together = ['student', 'course', 'semester']
        ordering = ['-semester', 'student']
    
    def __str__(self):
        # pylint: disable=no-member
        return f"{ self.student.name } - { self.course.code } ({ self.semester })"
