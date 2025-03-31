from django.db import models

# Create your models here.

class Course(models.Model):
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
        return f"{ self.name } ({ self.get_year_display() })"
    
    class Meta:
        ordering = ['name']

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=6, choices=Course.SEMESTER_CHOICES)
    grade = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        unique_together = ['student', 'course', 'semester']
        ordering = ['-semester', 'student']
    
    def __str__(self):
        return f"{ self.student.name } - { self.course.code } ({ self.semester })"
