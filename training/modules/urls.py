from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
path("",CourseModulesList.as_view(),name="modules_list"),
path("<uuid:pk>/",login_required(ModuleDetailView.as_view()),name="module_detail"),
path("<uuid:pk>/edit/",ModuleUpdateView.as_view(),name="module_edit"),
path("<uuid:pk>/delete/",ModuleDeleteView.as_view(),name="module_delete"),

path("add/",ModuleAddView.as_view(),name="module_add")
]
