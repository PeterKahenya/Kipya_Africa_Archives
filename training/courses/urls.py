from django.urls import path,include
from .views import *

urlpatterns = [
path("add/",AddCourseView.as_view(),name="add_course"),
path("",CoursesListView.as_view(),name="courses_list"),
path("<uuid:pk>/",CourseDetailView.as_view(),name="course_detail"),
path("<uuid:pk>/edit/",CourseUpdateView.as_view(),name="course_edit"),
path("<uuid:pk>/delete/",CourseDeleteView.as_view(),name="course_delete"),

path("<uuid:course>/modules/",include("modules.urls"))

]
