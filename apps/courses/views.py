from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from courses.models import Course
from operation.models import UserFavorite


class CoursesListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by('-create_time')
        hot_courses = Course.objects.all().order_by('-click_num')[0:3]
        sort = request.GET.get('sort', '')

        # 课程排序
        if sort == 'students':
            all_course = all_course.order_by('-students')
        elif sort == 'hot':
            all_course = all_course.order_by('-click_num')

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, per_page=3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {'all_course': courses, 'hot_courses': hot_courses, 'sort': sort})


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)
        else:
            relate_course = []

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        course.click_num += 1
        course.save()
        return render(request, 'course-detail.html',
                      {'course': course, 'relate_course': relate_course, 'has_fav_course': has_fav_course,
                       'has_fav_org': has_fav_org})
