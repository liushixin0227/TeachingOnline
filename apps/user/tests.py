from django.test import TestCase

# Create your tests here.
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TeachingOnline.settings")  # project_name 项目名称
django.setup()
from django.db.models import Q

from user.models import UserProfile

userlist = UserProfile.objects.filter(Q())
print(userlist)
