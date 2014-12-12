from django import forms

from jmbo.forms import as_div

from org.models import Signup, PetitionEntry


class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Email address"

    as_div = as_div


class SignPetitionForm(forms.ModelForm):

    class Meta:
        model = PetitionEntry

    as_div = as_div
