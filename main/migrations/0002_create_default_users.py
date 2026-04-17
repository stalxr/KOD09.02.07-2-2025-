from django.db import migrations
from django.contrib.auth import get_user_model


def create_default_users(apps, schema_editor):
    """Создание дефолтных пользователей"""
    User = get_user_model()
    
    # Создаем суперпользователя admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@masterpol.ru',
            password='admin123'
        )
        print('Created superuser: admin / admin123')
    
    # Создаем обычного пользователя manager
    if not User.objects.filter(username='manager').exists():
        User.objects.create_user(
            username='manager',
            email='manager@masterpol.ru',
            password='manager123'
        )
        print('Created user: manager / manager123')


def delete_default_users(apps, schema_editor):
    """Удаление дефолтных пользователей при откате"""
    User = get_user_model()
    User.objects.filter(username__in=['admin', 'manager']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_users, delete_default_users),
    ]
