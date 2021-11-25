import datetime
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Buy_a_ticket_Form(forms.Form):
    depart_date = forms.DateField(help_text="departure date")
    destination = forms.ForeignKeyField('Airport',on_delete = models.SET_NULL, null=True, related_name='destination')
    from_where = forms.ForeignKeyField('Airport',on_delete = models.SET_NULL, null=True, related_name='from_wh')

    def clean_depart_date(self):
            data = self.cleaned_data['depart_date']
            # Check if a date is not in the past.
            if data < datetime.date.today():
                raise ValidationError(_('Invalid date - departure in past'))
            # Remember to always return the cleaned data.
            return data
