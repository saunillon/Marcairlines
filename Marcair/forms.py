import datetime
from datetime import date
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail

from Marcair.models import Airport, Flight, Departure, Ticket, Connection, Transaction, Pilot, Employee, CrewMember, Airplane, Client

###########################################################################################

now = datetime.datetime.now()
YEAR_CHOICE = [now.year, now.year + 1]

class FlightForm(forms.ModelForm):
    # date_heure_depart = forms.DateTimeField()
    class Meta:
        model = Flight
        fields = (
            "connection_id",
            "departure_day",
        )
        widgets = {"departure_date": forms.SelectDateWidget(years=YEAR_CHOICE),}


class ResearchForm(forms.Form):
     """Form to research a flight"""
     destination = forms.ModelChoiceField(queryset=Airport.objects.filter(),
                                       label="Destination")
     class Meta:
        """ Link the form to the model Flight and define filters"""
        model = Flight
        fields = ("connection","departure_day")

class ReservationForm(forms.Form):
    """
    Form to create a reservation
    Args:
        last_name: Name of the client 
        first_name: first name of the client 
        email_address: email of the client to send the ticket 
        situation: First Class, Business Class or Economy Class situation souhaitée
    """
    FIRST = "F"
    ECONOMY = "E"
    BUSINESS = "B"

    SITUATIONS = [
        (FIRST, "First"),
        (ECONOMY, "Economy"),
        (BUSINESS, "Business")
    ]

    last_name = forms.CharField(max_length=100, disabled=True)
    first_name = forms.CharField(max_length=100, disabled=True)
    email_address = forms.EmailField(disabled=True)
    situation = forms.ChoiceField(required=False, choices=SITUATIONS)

    def __init__(self, Client, *args, **kwargs):
        """ Surcharge de la méthode init pour définir les champs initiaux du formulaire """
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = Client.first_name
        self.fields['last_name'].initial = Client.last_name
        self.fields['email_address'].initial = Client.email_address