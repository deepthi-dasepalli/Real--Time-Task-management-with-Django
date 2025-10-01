import os
import django

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskdash.settings')
import django
django.setup()

from django.contrib.auth.models import User

username = 'deepthi_dasepalli'
new_password = 'Deepthi'

try:
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    print(f"Password for user '{username}' has been reset successfully.")
except User.DoesNotExist:
    print(f"User '{username}' does not exist.")
