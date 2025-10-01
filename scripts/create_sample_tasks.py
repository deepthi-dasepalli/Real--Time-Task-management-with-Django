import os
import django
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskdash.settings')
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

def create_sample_tasks():
    # Get or create a user to assign tasks to
    user, created = User.objects.get_or_create(username='admin')
    if created:
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()

    # Create sample tasks
    Task.objects.create(
        title='Sample Task 1',
        description='This is a sample task 1',
        status='todo',
        priority='high',
        assigned_to=user,
        due_date=datetime.now() + timedelta(days=7)
    )
    Task.objects.create(
        title='Sample Task 2',
        description='This is a sample task 2',
        status='in_progress',
        priority='medium',
        assigned_to=user,
        due_date=datetime.now() + timedelta(days=14)
    )
    print("Sample tasks created successfully.")

if __name__ == '__main__':
    create_sample_tasks()
