from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class CoureseListView(View):
    def get(self, request):
        return render(request, 'course-list.html', {})
