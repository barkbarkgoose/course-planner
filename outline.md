# Course Planner Application Outline
## Technical Stack
- Django 4.x
- SQLite (for simplicity)
- Bootstrap (for basic styling... use CDN)
- Django Forms
- Django Admin 

## 1. Project Setup
- [x] Create Django project and app
- [x] Configure basic settings
- [x] Set up virtual environment
- [x] Create requirements.txt

## 2. Data Models
### Core Models
- [x] Course
  - Name
  - Code (e.g., CS101)
  - Description
  - Credits
  - Prerequisites (Many-to-Many relationship with self)
  - Semester offered (choices: Fall, Spring, Summer)

- [x] Student
  - Name
  - Email
  - Major
  - Year (Freshman, Sophomore, Junior, Senior)

- [x] Enrollment
  - Student (ForeignKey to Student)
  - Course (ForeignKey to Course)
  - Semester
  - Grade (optional)

## 3. Views and Templates
### Course Management
- [x] List all courses
- [x] View course details
- [ ] Add new course
- [ ] Edit existing coursewe'
- [ ] Delete course
- [ ] View prerequisites for each course

### Student Management
- [x] List all students
- [x] View student details
- [ ] Add new student
- [ ] Edit student information
- [ ] Delete student

### Enrollment Management
- [x] View student's enrolled courses
- [ ] Enroll student in courses
- [ ] Drop courses
- [ ] View grades

## 4. URLs and Routing
- [ ] Set up URL patterns for all views
- [ ] Create clean, RESTful URLs

## 5. Templates
- [x] Base template with navigation
- [x] Course list and detail templates
- [x] Student list and detail templates

### 5.1.
- [ ] Enrollment forms
- [ ] Forms for adding/editing courses and students

## 6. Admin Interface
- Register models in Django admin
- Customize admin interface for better usability

-----
# wrap up
## 7. Testing
- Basic model tests
- View tests
- URL tests

-----
# extras (later)
## 8. Future Enhancements (if time permits)
- User authentication
- Course scheduling conflicts
- GPA calculation
- Course recommendations based on major
- Export functionality for student records
- Course prerequisite validation
- Basic search functionality
- Simple filtering options

-----
# review

## Missing Elements to Consider:
### Forms:
- Using ModelForms for consistency
- Adding form validation
- Including helpful error messages
- Testing Strategy:
- Unit tests for models
- View tests for each endpoint
- Form validation tests
- URL pattern tests
- Template rendering tests

### Code Quality:
- Add type hints to functions
- Consider using class-based views for consistency
- Add logging for important operations
- Consider adding custom template tags for repeated logic