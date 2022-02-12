from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'add users'

    def handle(self, *args, **options):
        UserModel = get_user_model()

        if not UserModel.objects.filter(username='Robert').exists():
            user = UserModel.objects.create_user(
                'Robert', password='robert')
            user.is_superuser = True
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Daniel').exists():
            user = UserModel.objects.create_user(
                'Daniel', password='daniel')
            user.is_superuser = True
            user.is_staff = True
            user.save()

        print('user created')