from django.conf.urls import url
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
        views.StudentCourseDetailView.as_view(),
        name='student_course_detail'),
    url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
        views.StudentCourseDetailView.as_view(),
        name='student_course_detail_module'),
]


