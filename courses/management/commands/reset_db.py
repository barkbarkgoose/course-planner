from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Resets the database and loads sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Resetting database...')
        
        # Remove the database file if it exists
        db_path = 'db.sqlite3'
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write('Removed existing database')
        
        # Run migrations
        call_command('makemigrations', 'courses')
        call_command('migrate')
        self.stdout.write('Created fresh database')
        
        # Load sample data
        call_command('loaddata', 'sample_data.json')
        self.stdout.write('Loaded sample data')
        
        self.stdout.write(self.style.SUCCESS('Successfully reset database with sample data')) 