from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    url(r'^register/$',
        views.UserRegistrationView.as_view(),
        name='student-registration'),
    url('^enroll-course/$',
        views.StudentEnrollCourseView.as_view(),
        name='student-enroll-course'),
    url(r'^course/$',
        views.StudentCourseListView.as_view(),
        name='student_course_list'),
    url(r'^course/(?P<pk>\d+)/$',
        cache_page(300)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),
    url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
        cache_page(300)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'),
]


