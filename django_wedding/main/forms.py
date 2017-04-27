from django import forms
from main.models import Guest


class RSVPLoginForm(forms.Form):
    code = forms.CharField(label='Code', max_length=6)


class GuestRSVPForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['coming_private_ceremony',
                  'coming_public_ceremony',
                  'coming_reception',
                  'coming_dinner',
                  'coming_party']
