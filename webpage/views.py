from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template

from django.contrib.auth.models import User, Group

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['themelios01@gmail.com'],
                headers={'Reply To': contact_email}
            )

            email.send()

        return HttpResponse('<h2> Thank you. 빠른시일내에 답변해드리겠습니다.</h2>')

    else:
        return render(request, 'contact.html', {'form':Contact_Form })

def portfolio(request):
    return render(request, "portfolio.html")


def pricing(request):
    return render(request, "pricing.html")


def service(request):
    return render(request, "service.html")


def personal(request):
    return render(request, "personal.html")


def business(request):
    return render(request, "business.html")
