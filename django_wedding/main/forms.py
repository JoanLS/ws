from django import forms
from main.models import Guest, GuestComments, GuestChildren


class RSVPLoginForm(forms.Form):
    code = forms.CharField(label='Code', max_length=6)


class GuestRSVPForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # call constructor to set up the fields. If you don't do this 
        # first you can't modify fields.
        super(GuestRSVPForm, self).__init__(*args, **kwargs)

        try:
            if not self.instance.invited_private_ceremony:
                self.fields["coming_private_ceremony"].widget = forms.HiddenInput()                          
        except AttributeError:
            pass

        try:
            if not self.instance.invited_public_ceremony:
                self.fields["coming_public_ceremony"].widget = forms.HiddenInput()                          
        except AttributeError:
            pass

        try:
            if not self.instance.invited_reception:
                self.fields["coming_reception"].widget = forms.HiddenInput()                          
        except AttributeError:
            pass

        try:
            if not self.instance.invited_dinner:
                self.fields["coming_dinner"].widget = forms.HiddenInput()                          
        except AttributeError:
            pass

        try:
            if not self.instance.invited_party:
                self.fields["coming_party"].widget = forms.HiddenInput()                          
        except AttributeError:
            pass

    class Meta:
        model = Guest
        fields = ['coming_private_ceremony',
                  'coming_public_ceremony',
                  'coming_reception',
                  'coming_dinner',
                  'coming_party']

class GuestCommentsForm(forms.ModelForm):

    class Meta:
        model = GuestComments
        fields = ['dietary_restrictions', 'music_request', 'comments']

class GuestChildrenForm(forms.ModelForm):

    class Meta:
        model = GuestChildren
        fields = ['children_menus',]
