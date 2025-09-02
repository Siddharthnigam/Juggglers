from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                role='admin',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write('Admin user created successfully')
        else:
            self.stdout.write('Admin user already exists')