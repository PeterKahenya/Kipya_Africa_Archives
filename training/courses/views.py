from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Course
from modules.models import Module

class CoursesListView(ListView):
    template_name="courses/courses_list.html"
    context_object_name="courses_list"

    def get_queryset(self):
        return Course.objects.all()

class CourseDetailView(DetailView):
    model=Course
    template_name="courses/course_detail.html"

    def get_context_data(self, **kwargs):
        current_course=get_object_or_404(Course, id=self.kwargs['pk'])
        modules=Module.objects.filter(course=current_course)
        context = super().get_context_data(**kwargs)
        context['first_module'] = modules.first()
        context['course_modules'] = modules
        context['course'] = current_course
        return context



class AddCourseView(CreateView):
    model=Course
    fields=["title","description","image","price"]
    template_name="courses/course_add.html"
    success_url=reverse_lazy('courses_list')

class CourseUpdateView(UpdateView):
    template_name="courses/course_edit.html"
    model=Course
    fields=["title","description","image","price"]
    success_url="../"

class CourseDeleteView(DeleteView):
    model=Course
    success_url=reverse_lazy("courses_list")