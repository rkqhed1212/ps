from django import forms
from .models import *
from django.contrib.auth.models import User




# contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    id_contact_email = forms.EmailField(required=True)
    id_content= forms.CharField(required=True)