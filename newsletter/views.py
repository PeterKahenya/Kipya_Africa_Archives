from django.shortcuts import render
from django.views import View
from register.models import Attendee2020
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import datetime
from django.core.mail import EmailMessage
import uuid

receipt_no=0
invoice_no=0

class HomeView(View):

    def get(self, request):
        return render(request,"home.html",{"REGISTERED":False},None,None,None)
    def post(self,request):
        title=request.POST.get("title")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        organization=request.POST.get("organization")
        job_title=request.POST.get("job_title")
        role=request.POST.get("role")
        country=request.POST.get("country")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        is_paid=request.POST.get("is_paid")
        mpesa_code=request.POST.get("mpesa_code")
        mpesa_name=request.POST.get("mpesa_name")
        mpesa_amount=request.POST.get("mpesa_amount")

        attendee=Attendee2020()
        attendee.title=title
        attendee.first_name=first_name
        attendee.last_name=last_name
        attendee.organization=organization
        attendee.job_title=job_title
        attendee.role=role
        attendee.country=country
        attendee.email=email
        attendee.phone=phone


        if is_paid=="YES":
            attendee.mpesa_code=mpesa_code
            attendee.mpesa_name=mpesa_name
            attendee.mpesa_amount=mpesa_amount
            attendee.save()
            receipt=self.prepare_receipt(attendee)

            subject="EACOSH 2020 Payment Receipt"
            html_message = render_to_string('payment_response_email.html', {'attendee': attendee })
            plain_message = strip_tags(html_message)
            from_email = 'EACOSH 2020 <info@eacosh.com>'
            to = email
            message = EmailMessage(
                subject,
                html_message,
                from_email,
                [to],
                [],
                reply_to=['info@eacosh.com'],
                headers={'Message-ID': str(uuid.uuid4()) },
                attachments=[
                    ("EACOSH_2020_PAYMENT_RECEIPT.pdf",open(receipt,"rb").read(),'application/pdf')
                ]
                )
            message.content_subtype = "html"
            message.send()
            return render(request,"home.html",{"REGISTERED":True},None,None,None)
            
        else:
            attendee.save()
            pfi_delegate=self.prepare_pfis(attendee,"delegate")
            pfi_excursion=self.prepare_pfis(attendee,"excursion")
            
            pfi_goldsponsor=self.prepare_pfis(attendee,"goldsponsor")
            pfi_exhibitor=self.prepare_pfis(attendee,"exhibitor")
            pfi_silversponsor=self.prepare_pfis(attendee,"silversponsor")


            eacosh_program=os.path.join(settings.MEDIA_ROOT,"files/eacosh_2020_program.pdf")
            eacosh_concept_note=os.path.join(settings.MEDIA_ROOT,"files/eacosh_2020_concept_note.pdf")

            subject="East Africa Conference on Occupational Safety and Health EACOSH Registration"
            html_message = render_to_string('response_with_pfi.html', {'attendee': attendee,"pfi_delegate_name":os.path.basename(pfi_delegate),"pfi_excursion_name":os.path.basename(pfi_excursion) })
            plain_message = strip_tags(html_message)
            from_email = 'EACOSH 2020 <info@eacosh.com>'
            to = email
            message = EmailMessage(
                subject,
                html_message,
                from_email,
                [to],
                [],
                reply_to=['info@eacosh.com'],
                headers={'Message-ID': str(uuid.uuid4()) },
                attachments=[
                    ("EACOSH_2020_DELEGATE_Invoice.pdf",open(pfi_delegate,"rb").read(),'application/pdf'),
                    ("EACOSH__2020_EXCUSION_Invoice.pdf",open(pfi_excursion,"rb").read(),'application/pdf'),

                    ("EACOSH__2020_GOLDSPONSOR_Invoice.pdf",open(pfi_goldsponsor,"rb").read(),'application/pdf'),
                    ("EACOSH__2020_SILVERSPONSOR_Invoice.pdf",open(pfi_silversponsor,"rb").read(),'application/pdf'),
                    ("EACOSH__2020_EXHIBITION_Invoice.pdf",open(pfi_exhibitor,"rb").read(),'application/pdf'),
                    
                    ("EACOSH_2020_DRAFT_PROGRAM.pdf",open(eacosh_program,"rb").read(),'application/pdf'),
                    ("EACOSH_2020_CONCEPT_NOTE.pdf",open(eacosh_concept_note,"rb").read(),'application/pdf')
                            ]
                )
            message.content_subtype = "html"
            message.send()
            return render(request,"home.html",{"REGISTERED":True},None,None,None)
            
    def link_callback(self,uri, rel):

        sUrl = settings.STATIC_URL      
        sRoot = settings.STATIC_ROOT    
        mUrl = settings.MEDIA_URL      
        mRoot = settings.MEDIA_ROOT    

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        if not os.path.isfile(path):
                raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

    def get_invoice_no(self):
        global invoice_no
        day=datetime.datetime.today().day
        if day<10:
            day="0"+str(day)
        month=datetime.datetime.today().month
        if month<10:
            month="0"+str(month)
        current=invoice_no
        if invoice_no<10:
            current="0"+str(invoice_no)
        invoice=str(datetime.datetime.today().year)+str(month)+str(day)+str(current)
        invoice_no+=1
        return invoice
        
    def get_receipt_no(self):
        global receipt_no
        day=datetime.datetime.today().day
        if day<10:
            day="0"+str(day)
        month=datetime.datetime.today().month
        if month<10:
            month="0"+str(month)
        current=receipt_no
        if receipt_no<10:
            current="0"+str(receipt_no)
        receipt=str(datetime.datetime.today().year)+str(month)+str(day)+str(current)
        receipt_no+=1
        return receipt
        
    def prepare_receipt(self,attendee):
        template = get_template('receipt.html')
        context = {'receipt_no':self.get_receipt_no() ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        html = template.render(context)
        receipt_file_path=os.path.join(settings.MEDIA_ROOT,"receipts/"+attendee.first_name+attendee.last_name+"Receipt"+self.get_receipt_no()+".pdf")
        receipt_file = open(receipt_file_path, "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=receipt_file, link_callback=self.link_callback)
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        receipt_file.close()
        return receipt_file_path
    
    def prepare_pfis(self,attendee,type_of_attendee,):
        print("generated PFI")
        my_invoice_no=self.get_invoice_no()
        template = get_template('pfi.html')

        context = {'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        if type_of_attendee=="delegate":
            context = {'is_delegate':True,'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        elif type_of_attendee=="excursion":
            context = {'is_excursion':True,'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        elif type_of_attendee=="goldsponsor":
            context = {'is_goldsponsor':True,'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        elif type_of_attendee=="exhibitor":
            context = {'is_exhibitor':True,'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        elif type_of_attendee=="silversponsor":
            context = {'is_silversponsor':True,'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        else:
            context = {'type_of_attendee':type_of_attendee,'invoice_no':my_invoice_no ,'attendee':attendee,'date':datetime.datetime.today().strftime('%d/%m/%Y')}
        
        html = template.render(context)
        receipt_file_path=os.path.join(settings.MEDIA_ROOT,"invoices/"+attendee.first_name+attendee.last_name+"Invoice"+my_invoice_no+".pdf")
        receipt_file = open(receipt_file_path, "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=receipt_file, link_callback=self.link_callback)
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        receipt_file.close()
        return receipt_file_path

