import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'master_pol.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Удаляем старого если есть
User.objects.filter(username='admin').delete()

# Создаём нового
user = User.objects.create_superuser('admin', '', 'admin123')
print(f'Success! User created: {user.username}')
print('Login: admin')
print('Password: admin123')
