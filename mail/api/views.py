from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email
from django.core.mail import EmailMessage
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SendEmailView(APIView):
	"""docstring for SendEmailView"""

	def post(self,request,format=None):
		print(request.data)
		print(type(request.data))

		send_email.delay(
				subject=request.data.get("subject"),
				from_email=request.data.get("from_email"),
				body=request.data.get("body"),
				cc=request.data.get("cc"),
				reply_to=request.data.get("reply_to"),
				to=request.data.get("to"),
				bcc=request.data.get("bcc"),
				attachments=request.data.get("attachments")
				)
		return Response({'data':request.data})
