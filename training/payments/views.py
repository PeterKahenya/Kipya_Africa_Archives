from django.shortcuts import render,redirect
from django.views import View
import stripe
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from courses.models import Course
from django.core.mail import send_mail





class PaymentOptionsPage(View):
    def get(self,request):
        if request.GET.get('order_id'):
            return render(request,"payments/payment_options.html",{"order_id":request.GET.get('order_id'),"next":request.GET.get('next'),"purpose":request.GET.get('purpose')})
        else:
            return redirect("../")


@method_decorator(csrf_exempt, name='dispatch')
class MPESAPaymentPage(View):
    def get(self,request):
        if request.GET.get('order_id'):
            if request.GET.get('purpose')=="course":
                course=Course.objects.get(pk=request.GET.get('order_id'))
            else:
                return redirect("../")
            return render(request,"payments/payment_option_mpesa.html",{"order_id":request.GET.get('order_id'),"purpose_object":course})
        else:
            return redirect("../")
    def post(self,request):
            course=Course.objects.get(id=request.GET.get('order_id'))

            payment=Payment()
            payment.course=course
            payment.payment_method="MPESA"
            payment.user=request.user
            payment.code=request.POST.get('mpesa_code')
            payment.amount=request.POST.get('mpesa_amount')
            payment.account_no=request.POST.get('mpesa_name')

            payment.save()
            print(str(request.POST.get('mpesa_amount'))+"--"+str(course.price))
            print(float(request.POST.get('mpesa_amount'))<float(course.price))
            if float(request.POST.get('mpesa_amount'))<float(course.price):
                send_mail('KIPYA ONLINE TRAINING PAYMENT','Your Payment for <strong>'+course.title+' </strong> Has been received. However, Please note that the amount sent is insufficient. You will be refunded soon with the transaction deducted from the amount sent','info@kipya-africa.com',[request.user.email],fail_silently=False)
                return render(request,"profile.html",{"message":"Your Payment WAS INSUFFICIENT! YOU WILL BE REFUNDED AT A COST TO YOU!"})
            else:
                course.enrollees.add(request.user)
                send_mail('KIPYA ONLINE TRAINING PAYMENT','Your Payment for <strong>'+course.title+' </strong> Has been received. Your enrollment is is successfull. Welcome onboard','info@kipya-africa.com',[request.user.email],fail_silently=False)
                return redirect(request.GET.get('next'))


# @method_decorator(csrf_exempt, name='dispatch')
class CardPaymentPage(View):

    def get(self,request):
        if request.GET.get('order_id'):
            return render(request,"payments/payment_option_card.html",{"order_id":request.GET.get('order_id')})
        else:
            return redirect("../")
            
    def post(self,request):
        stripe.api_key = 'sk_test_O5YURM28jBMM9E6GdrdzKz5W00hhfajUK0'
        token=request.POST.get("stripeToken")

        try:
            charge = stripe.Charge.create(
                amount=999,
                currency='usd',
                description='Example charge',
                source=token,
            )
            course=Course.objects.get(id=request.GET.get('order_id'))
            payment=Payment()
            payment.course=course
            payment.payment_method="CARD"
            payment.user=request.user
            payment.code=charge["id"]
            payment.amount=charge["amount"]
            payment.account_no=request.user.id
            payment.save()

            course.enrollees.add(request.user)
            

        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught

            # print('Status is: %s' % e.http_status)
            # print('Type is: %s' % e.error.type)
            # print('Code is: %s' % e.error.code)
            # # param is '' in this case
            # print('Param is: %s' % e.error.param)
            # print('Message is: %s' % e.error.message)
            return render(request,"payments/card_error_page.html",{"error":e})
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            return render(request,"payments/card_error_page.html",{"error":e})
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            return render(request,"payments/card_error_page.html",{"error":e})
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            return render(request,"payments/card_error_page.html",{"error":e})
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            return render(request,"payments/card_error_page.html",{"error":e})
        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            return render(request,"payments/card_error_page.html",{"error":e})
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            return render(request,"payments/card_error_page.html",{"error":e})
        return render(request,"payments/card_success_page.html",{"next":request.GET.get('next')})
        

class PaypalPaymentPage(View):
    def get(self,request):
        if request.GET.get('order_id'):
            return render(request,"payments/payment_option_paypal.html",{"order_id":request.GET.get('order_id')})
        else:
            return redirect("../")

    