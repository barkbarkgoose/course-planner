from django.apps import AppConfig


class CoursesConfig(AppConfig):
    """
    Configuration class for the courses application.
    
    This class is required by Django to:
    1. Identify the courses app as a Django application
    2. Configure app-specific settings (like the default primary key field type)
    3. Enable Django's application registry to properly load and manage the app
    
    The default_auto_field setting ensures consistent primary key field types
    across all models in the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
