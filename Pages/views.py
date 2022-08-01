from re import S
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pyparsing import Opt
from django.http import HttpResponseRedirect
from .models import Option,Service,Discount
from django.contrib import messages 
from django.urls import reverse
from django.db import connection
from email_validator import (
    validate_email,
    EmailNotValidError
)
from langdetect import detect


# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get("optionTitle") != "" and request.POST.get("optionTitle") is not None:
            optionTitle = request.POST.get("optionTitle")
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        elif request.POST.get("langTitle") != "" and request.POST.get("langTitle") is not None:
            if detect(request.POST.get("langTitle")) != 'ar':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/option.html', args)
        elif request.POST.get("serviceTitle") != "" and request.POST.get("serviceTitle") is not None:
            if request.POST.get("pageLang") != 'ar':
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitle = %s'], params= [request.POST.get("serviceTitle")])[0]
                return render(request, 'pages/service.html', args)
            else:
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitleAR = %s'], params= [request.POST.get("serviceTitle")])[0]
                return render(request, 'pages/servicear.html', args)
        elif request.POST.get("serTitle") != "" and request.POST.get("serTitle") is not None:
            if request.POST.get("serLang") != 'ar':
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitle = %s'], params= [request.POST.get("serTitle")])[0]
                return render(request, 'pages/servicear.html', args)
            else:
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitleAR = %s'], params= [request.POST.get("serTitle")])[0]
                return render(request, 'pages/service.html', args)
    else:
        args = {}
        args['Services'] = Service.objects.all()
        args['Discounts'] = Discount.objects.all()
        return render(request, 'pages/index.html', args)
    
def indexar(request):
    if request.method == 'POST':
        if request.POST.get("optionTitle") != "" and request.POST.get("optionTitle") is not None:
            optionTitle = request.POST.get("optionTitle")
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        elif request.POST.get("langTitle") != "" and request.POST.get("langTitle") is not None:
            if detect(request.POST.get("langTitle")) != 'ar':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/option.html', args)
        elif request.POST.get("serviceTitle") != "" and request.POST.get("serviceTitle") is not None:
            if request.POST.get("pageLang") != 'ar':
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitle = %s'], params= [request.POST.get("serviceTitle")])[0]
                return render(request, 'pages/service.html', args)
            else:
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitleAR = %s'], params= [request.POST.get("serviceTitle")])[0]
                return render(request, 'pages/servicear.html', args)
        elif request.POST.get("serTitle") != "" and request.POST.get("serTitle") is not None:
            if request.POST.get("serLang") != 'ar':
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitle = %s'], params= [request.POST.get("serTitle")])[0]
                return render(request, 'pages/servicear.html', args)
            else:
                args = {}
                args['service'] = Service.objects.all().extra(where=['serviceTitleAR = %s'], params= [request.POST.get("serTitle")])[0]
                return render(request, 'pages/service.html', args)
    else:
        args = {}
        args['Services'] = Service.objects.all()
        args['Discounts'] = Discount.objects.all()
        return render(request, 'pages/indexar.html', args)

def contactus(request):
    if request.method == 'POST':
        if request.POST.get("email") == "true":
            #Send Message to Myself
            Subject = request.POST.get("Subject")
            Message = request.POST.get("Message")
            send_mail(
                subject=Subject,
                message=Message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS],
                html_message=Message 
            )
            #Send Message to Recipient
            subject = "Email Received"
            html_message = render_to_string('core/emailtemplate.html', {'context': 'values'})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = request.POST.get("SendEmail")
            try:
                valid_result = validate_email(to)
                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                return render(request, 'pages/index.html')
            except EmailNotValidError as e:
                messages.error(request, "Enter a valid email address!")
                return render(request, 'pages/contactus.html')
        elif request.POST.get("optionTitle") != "":
            optionTitle = request.POST.get("optionTitle")            
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        elif request.POST.get("langTitle") != "":
            if detect(request.POST.get("langTitle")) != 'ar':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/option.html', args) 
    else:
        return render(request, 'pages/contactus.html')

def contactusar(request):
    if request.method == 'POST':
        if request.POST.get("email") == "true":
            #Send Message to Myself
            Subject = request.POST.get("Subject")
            Message = request.POST.get("Message")
            send_mail(
                subject=Subject,
                message=Message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS],
                html_message=Message 
            )
            #Send Message to Recipient
            subject = "Email Received"
            html_message = render_to_string('core/emailtemplate.html', {'context': 'values'})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = request.POST.get("SendEmail")
            try:
                valid_result = validate_email(to)
                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                return render(request, 'pages/indexar.html')  
            except EmailNotValidError as e:
                messages.error(request, "ادخل بريد الكتروني صحيح!")
                return render(request, 'pages/contactusar.html')  
  
        if request.POST.get("optionTitle") != "":
            optionTitle = request.POST.get("optionTitle")
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        if request.POST.get("langTitle") != "":
                if detect(request.POST.get("langTitle")) != 'ar':
                    args = {}
                    args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                    return render(request, 'pages/optionar.html', args)
                else:
                    args = {}
                    args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                    return render(request, 'pages/option.html', args)    
    else:
        return render(request, 'pages/contactusar.html')

############
def values(request):
    if request.method == 'POST':
        if request.POST.get("optionTitle") != "":
            optionTitle = request.POST.get("optionTitle")            
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        if request.POST.get("langTitle") != "":
            if detect(request.POST.get("langTitle")) != 'ar':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                return render(request, 'pages/option.html', args) 
    else:
        return render(request, 'pages/values.html')

def valuesar(request):
    if request.method == 'POST':
        if request.POST.get("optionTitle") != "":
            optionTitle = request.POST.get("optionTitle")
            if optionTitle[-1] == '+':
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle[:-1]])[0]
                return render(request, 'pages/optionar.html', args)
            else:
                args = {}
                args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [optionTitle])[0]
                return render(request, 'pages/option.html', args)
        if request.POST.get("langTitle") != "":
                if detect(request.POST.get("langTitle")) != 'ar':
                    args = {}
                    args['option'] = Option.objects.all().extra(where=['optionTitle = %s'], params= [request.POST.get("langTitle")])[0]
                    return render(request, 'pages/optionar.html', args)
                else:
                    args = {}
                    args['option'] = Option.objects.all().extra(where=['optionTitleAR = %s'], params= [request.POST.get("langTitle")])[0]
                    return render(request, 'pages/option.html', args)    
    else:
        return render(request, 'pages/valuesar.html')
############

def service(request):
    return render(request, 'pages/service.html')

def servicear(request):
    return render(request, 'pages/servicear.html')

def option(request):
        return render(request, 'pages/option.html', args)

def optionar(request):
        return render(request, 'pages/optionar.html', args)