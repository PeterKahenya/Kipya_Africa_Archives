from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(NewslettersList.as_view()),name="newsletters-list"),
    path('<uuid:pk>/', login_required(NewsletterDetail.as_view())),
    path('<uuid:pk>/edit', login_required(NewsletterEdit.as_view())),
    path('<uuid:pk>/delete',login_required(NewsletterDelete.as_view())),
    path('<uuid:pk>/send', login_required(SendNewsletter.as_view())),
    path('<uuid:pk>/test',login_required(SendTestNewsletter.as_view())),

    path('<uuid:newsletter_id>/posts/<uuid:pk>/edit', login_required(PostEdit.as_view())),
    path('<uuid:newsletter_id>/posts/<uuid:pk>/delete', login_required(PostDelete.as_view())),

]
