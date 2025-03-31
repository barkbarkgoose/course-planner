# Course Planner Application

A Django-based course planning application that allows users to manage courses, students, and enrollments. This project serves as a demonstration of Django fundamentals and best practices.

## Project Setup

1. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ to access the application.

## Project Structure

```
course-planner/
├── main/                  # Project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── courses/             # Main application
│   ├── admin.py        # Admin interface configuration
│   ├── apps.py         # App configuration
│   ├── models.py       # Data models
│   ├── views.py        # View functions
│   ├── urls.py         # App URL routing
│   ├── management/     # Custom management commands
│   │   └── commands/
│   │       └── reset_db.py
│   └── fixtures/       # Sample data
│       └── sample_data.json
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   └── courses/       # App-specific templates
│       ├── course_list.html
│       ├── course_detail.html
│       ├── student_list.html
│       ├── student_detail.html
│       └── enrollment_list.html
└── manage.py          # Django management script
```

## Sample Data

The project includes sample data for testing and demonstration purposes. To load the sample data:

1. **Reset database and load sample data**
   ```bash
   python manage.py reset_db
   ```

This command will:
- Remove the existing database
- Run migrations
- Load sample data including:
  - 4 courses (CS101, CS201, CS301, CS401)
  - 3 students
  - 4 enrollments

## Features

- Course management (view, list)
- Student management (view, list)
- Enrollment tracking
- Admin interface for data management
- Bootstrap-based responsive UI
- RESTful URL structure

-----

## Testing Suggestions

### Model Tests
```python
# test_models.py
from django.test import TestCase
from .models import Course, Student, Enrollment

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            name="Test Course",
            code="TEST101",
            credits=3,
            semester_offered="FALL"
        )
        self.assertEqual(course.code, "TEST101")
        self.assertEqual(course.credits, 3)

class StudentModelTest(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(
            name="Test Student",
            email="test@example.com",
            major="Computer Science",
            year="FR"
        )
        self.assertEqual(student.name, "Test Student")
        self.assertEqual(student.get_year_display(), "Freshman")

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Test Student",
            email="test@example.com",
            major="CS",
            year="FR"
        )
        self.course = Course.objects.create(
            name="Test Course",
            code="TEST101",
            credits=3,
            semester_offered="FALL"
        )

    def test_enrollment_creation(self):
        enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            semester="FALL"
        )
        self.assertEqual(enrollment.student, self.student)
        self.assertEqual(enrollment.course, self.course)
```

### View Tests
```python
# test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Course, Student

class CourseViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(
            name="Test Course",
            code="TEST101",
            credits=3,
            semester_offered="FALL"
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_list.html')

    def test_course_detail_view(self):
        response = self.client.get(
            reverse('courses:course_detail', args=[self.course.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_detail.html')
```

### URL Tests
```python
# test_urls.py
from django.test import TestCase
from django.urls import reverse, resolve
from . import views

class UrlsTest(TestCase):
    def test_course_list_url(self):
        url = reverse('courses:course_list')
        self.assertEqual(resolve(url).func, views.course_list)

    def test_course_detail_url(self):
        url = reverse('courses:course_detail', args=[1])
        self.assertEqual(resolve(url).func, views.course_detail)
```

## Future Improvements

1. **Forms and Validation**
   - Add forms for creating/editing courses and students
   - Implement form validation
   - Add custom validation for prerequisites

2. **Authentication**
   - Add user authentication
   - Implement role-based access control
   - Add login/logout functionality

3. **API Development**
   - Create REST API endpoints
   - Add API documentation
   - Implement API authentication

4. **Additional Features**
   - Course scheduling conflict detection
   - GPA calculation
   - Course recommendations
   - Export functionality

5. **Testing**
   - Add more comprehensive test coverage
   - Implement integration tests
   - Add test fixtures

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 