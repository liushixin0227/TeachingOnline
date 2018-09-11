import json

from django.http import HttpResponse
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View

from organization.forms import UserAskForm
from organization.models import CourseOrg, CityDict


# Create your views here.

class OrgView(View):
    @staticmethod
    def get(request):
        all_orgs = CourseOrg.objects.all()
        all_city = CityDict.objects.all()
        city_id = request.GET.get('city', '')
        category = request.GET.get('ct', '')
        sort = request.GET.get('sort', '')
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        if category:
            all_orgs = all_orgs.filter(category=category)

        if sort == 'students':
            all_orgs = all_orgs.order_by('-student_num')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-course_nums')

        org_count = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=1, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'orgs': orgs,
            'all_city': all_city,
            'org_count': org_count,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })


class AddUserAskView(View):
    @staticmethod
    def post(request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save()
            return HttpResponse('{"status": "success"}', content_type="application/json")
        else:
            return HttpResponse('{"status": "fail", "msg": "提交错误"}', content_type="application/json")


class OrgHomeView(View):
    current_page = 'Home'

    @classmethod
    def get(cls, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page': cls.current_page
        })


class OrgCourseView(View):
    current_page = 'Course'

    @classmethod
    def get(cls, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': cls.current_page,
        })


class OrgDescribeView(View):
    current_page = 'Describe'

    @classmethod
    def get(cls, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': cls.current_page,
        })
