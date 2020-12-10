# Create your tasks here

from celery import shared_task
from django.core.mail import EmailMessage
import uuid



@shared_task
def send_email(subject,from_email, to, cc, bcc,reply_to, body, attachments):
	attachments_tuples=[]

	for attachment in attachments:
		filename,path,mimetype=attachment[0],attachment[1],attachment[2]
		attachments_tuples.append((filename,open(path),mimetype))

	message = EmailMessage(
			subject=subject,
			body=body,
			reply_to=reply_to,
			from_email=from_email,
			to=to,
			bcc=bcc,
			attachments=attachments_tuples,
			headers={'Message-ID': str(uuid.uuid4())
			})

	message.content_subtype = "html"

	try:
		message.send()
	except Exception as e:
		return e
	else:
		return {"success":True}
	finally:
		pass