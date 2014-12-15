from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect

from org.models import Signup
from org.forms import SignupForm, SignPetitionForm


def home(request):
    if request.method == "POST":
        form = SignPetitionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse("sign-petition-success"))
    else:
        form = SignPetitionForm()

    extra = dict(form=form)
    return render_to_response(
       "org/home.html",
        extra,
        context_instance=RequestContext(request)
    )
