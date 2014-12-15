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

    def clean(self):
        cleaned_data = super(SignPetitionForm, self).clean()
        
        email = cleaned_data.get("email")
        mobile_number = cleaned_data.get("mobile_number")

        if not email and not mobile_number:
            error_msg = "You must include at least one contact field."
            raise forms.ValidationError(error_msg)

        return cleaned_data
        

    class Meta:
        model = PetitionEntry

    as_div = as_div
