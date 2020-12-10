from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Newsletter,Post
from django.core.mail import EmailMessage
import uuid
from .tasks import send_newsletter,test_newsletter
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from subscribers.models import Subscriber



class NewslettersList(View):
    def get(self,request):
        return render(request,"newsletters_list.html", {"newsletters":Newsletter.objects.all()},None,None,None)
    def post(self,request):
        newsletter_name=request.POST.get("newsletter_name")
        newsletter=Newsletter()
        newsletter.newsletter_name=newsletter_name
        newsletter.save()
        if newsletter:
            return redirect("/newsletters/"+str(newsletter.id)+"/edit")


class NewsletterDetail(View):
    def get(self,request,pk):
        newsletter=Newsletter.objects.get(id=pk)
        posts=Post.objects.filter(newsletter=newsletter).order_by('created')
        return render(request,"newsletter_detail.html", {"newsletter":newsletter,"posts":posts,"EDITING":True},None,None,None)


class NewsletterEdit(View):
    def get(self,request,pk):
        newsletter=Newsletter.objects.get(id=pk)
        posts=Post.objects.filter(newsletter=newsletter).order_by('created')
        return render(request,"newsletter_edit.html",{"newsletter":newsletter,"posts":posts})

    def post(self,request,pk):
        content=request.POST.get("content")
        newsletter = Newsletter.objects.get(id=pk)
        new_post=Post()
        new_post.content=content
        new_post.newsletter=newsletter
        new_post.save()

        posts=Post.objects.filter(newsletter=newsletter).order_by('created')
        return render(request,"newsletter_edit.html",{"newsletter":newsletter,"posts":posts})

class NewsletterDelete(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletters-list')
    template_name="newsletter_confirm_delete.html"

@method_decorator(csrf_exempt, name='dispatch')
class SendTestNewsletter(View):
    def post(self,request,pk):
        print("SENDING TEST NEWSLETTER")
        newsletter=Newsletter.objects.get(id=pk)
        posts=Post.objects.filter(newsletter=newsletter).order_by('created')
        data=json.loads(request.body.decode('utf-8'))
        test_address=data["test_address"]
        scheme=request.scheme
        host=request.META["HTTP_HOST"]
        test_newsletter(pk,test_address,scheme,host)
        
        return JsonResponse({"TEST_SENT":True })

        

class SendNewsletter(View):
    def get(self,request,pk):
        newsletter=Newsletter.objects.get(id=pk)
        posts=Post.objects.filter(newsletter=newsletter)
        subscribers=Subscriber.objects.all()

        return render(request,"send_newsletter.html",
                                {
                                "newsletter":newsletter,
                                "posts":posts,
                                "subscribers":subscribers
                                })
    def post(self,request,pk):
        newsletter=Newsletter.objects.get(id=pk)
        posts=Post.objects.filter(newsletter=newsletter)
        subscribers=Subscriber.objects.all()
        scheme=request.scheme
        host=request.META["HTTP_HOST"]
        if(send_newsletter(pk,scheme,host)):
            return render(request,"send_newsletter.html",
                                {
                                "queued":True,
                                "newsletter":newsletter,
                                "posts":posts,
                                "subscribers":subscribers
                })
        
        else:
            return render(request,"send_newsletter.html",
                                {
                                "queued":False,
                                "newsletter":newsletter,
                                "posts":posts,
                                "subscribers":subscribers
            })

        



class PostEdit(UpdateView):
    model = Post
    fields = ['content']
    success_url="../../edit"


class PostDelete(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url="../../edit"
