from django.urls import path,include
from .views import *

urlpatterns = [
    path("",PaymentOptionsPage.as_view(),name="payment_options_list"),
    path("mpesa/",MPESAPaymentPage.as_view(),name="payment_option_mpesa"),
    path("credit_and_debit_card/",CardPaymentPage.as_view(),name="payment_option_card"),
    path("paypal/",PaypalPaymentPage.as_view(),name="payment_option_paypal")

]