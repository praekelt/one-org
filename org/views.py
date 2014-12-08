from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect

from org.models import Signup
from org.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            obj = form.save()
            msg = _("You have successfully joined One.")
            messages.success(request, msg, fail_silently=True)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignupForm()

    extra = dict(form=form)
    return render_to_response(
       "org/signup_tile.html",
        extra,
        context_instance=RequestContext(request)
    )
