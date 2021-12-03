import datetime
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail

from Marcair.models import Airport, Flight, Departure, Ticket, Connection, Transaction, Pilot, Employee, CrewMember, Airplane, Client

@login_required
class Buy_a_ticket_Form(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


class IdentityForm(forms.Form):
    model = Client
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    adress = forms.CharField(label='Adress', max_length=100)
    email_adress = forms.EmailField(label='Email')
    group = forms.MultipleChoiceField(label='Group')
    def __str__(self):
        return f'{self.first_name}, {self.last_name},{self.adress},{self.email_adress},{self.group}'