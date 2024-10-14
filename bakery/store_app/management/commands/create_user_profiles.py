# # your_app/management/commands/create_user_profiles.py

# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from store_app.models import UserProfile

# class Command(BaseCommand):
#     help = 'Creates UserProfile instances for users without profiles'

#     def handle(self, *args, **options):
#         users_without_profile = User.objects.filter(userprofile__isnull=True)
#         for user in users_without_profile:
#             UserProfile.objects.create(user=user)
#         self.stdout.write(self.style.SUCCESS('Successfully created UserProfiles'))
