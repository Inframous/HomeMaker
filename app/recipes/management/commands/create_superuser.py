from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os 

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ.get('SUPERUSER_NAME')).exists():
            User.objects.create_superuser(os.environ.get('SUPERUSER_NAME'), os.environ.get('SUPERUSER_EMAIL'), os.environ.get('SUPERUSER_PASS'))
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))

