from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from courses.models import Course
from .models import Module
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin


class CourseModulesList(ListView):
    template_name = 'modules/modules_list.html'
    context_object_name="modules_list"


    def get_queryset(self):
        self.course = get_object_or_404(Course, id=self.kwargs['course'])
        return Module.objects.filter(course=self.course)


class ModuleDetailView(UserPassesTestMixin,DetailView):
    template_name = 'modules/module_detail.html'
    model=Module
    

    def test_func(self):
        self.course = get_object_or_404(Course, id=self.kwargs['course'])
        if self.request.user in self.course.enrollees.all():
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect("/payments/?order_id="+str(self.course.id)+"&purpose=course&next="+self.request.path)

    def get_context_data(self, **kwargs):
        current_course=get_object_or_404(Module, id=self.kwargs['pk']).course
        modules=Module.objects.filter(course=current_course)
        context = super().get_context_data(**kwargs)
        context['modules_list'] = modules
        context['current_course'] = current_course
        next_module=None
        prev_module=None

        current_module_index=list(modules).index(get_object_or_404(Module, id=self.kwargs['pk']))
        
        if current_module_index!=0:
            prev_module=modules[current_module_index-1]
        if current_module_index!=len(list(modules))-1:
            next_module=modules[current_module_index+1]

        if self.request.user not in get_object_or_404(Module, id=self.kwargs['pk']).users.all():
            get_object_or_404(Module, id=self.kwargs['pk']).users.add(self.request.user)
        
        context['next_module'] = next_module
        context['prev_module'] = prev_module

        return context

class ModuleUpdateView(UpdateView):
    template_name="modules/module_edit.html"
    model=Module
    fields=["title","description","content"]

class ModuleDeleteView(DeleteView):
    model=Module
    success_url="../../"

class ModuleAddView(CreateView):
    model=Module
    fields=["course","title","description","content"]
    template_name="modules/module_add.html"
    success_url="../"

    def get_queryset(self):
        self.course = get_object_or_404(Course, id=self.kwargs['course'])  
    
    def form_valid(self, form):
        form.instance.course = get_object_or_404(Course, id=self.kwargs['course'])
        return super(ModuleAddView, self).form_valid(form)