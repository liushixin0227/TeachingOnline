from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View

from organization.models import CourseOrg, CityDict


# Create your views here.

class OrgView(View):
    @staticmethod
    def get(request):
        all_orgs = CourseOrg.objects.all()
        all_city = CityDict.objects.all()
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
        })
