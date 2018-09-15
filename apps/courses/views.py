from django.shortcuts import render
# Create your views here.
from django.views.generic import View

from courses.models import Course


class CoursesListView(View):
    def get(self, request):
        all_course = Course.objects.all()
        return render(request, 'course-list.html', {'all_course': all_course, })
