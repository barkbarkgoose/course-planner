from django.contrib import admin
from .models import Course, Student, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits', 'semester_offered')
    list_filter = ('semester_offered',)
    search_fields = ('code', 'name', 'description')
    filter_horizontal = ('prerequisites',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'major', 'year')
    list_filter = ('year', 'major')
    search_fields = ('name', 'email', 'major')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'grade')
    list_filter = ('semester', 'grade')
    search_fields = ('student__name', 'course__code', 'course__name')
    raw_id_fields = ('student', 'course')
