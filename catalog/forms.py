from django import forms
import datetime

from .models import BookInstance
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Form class is very flexible
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    # The easiest way to validate a single field is to override the
    # method clean_<fieldname>() for the field you want to check
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks'))
        
        return data


# ModelForms is simpler choice if you just need a form to map the fields of a single model
class RenewBookModelForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back']