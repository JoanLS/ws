# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import RSVPLoginForm
from django.urls import reverse
from main.models import GuestCode


class Homepage(TemplateView):
    template_name = "home.html"


class RSVPLogin(FormView):
    template_name = 'rsvp_login.html'
    form_class = RSVPLoginForm
    success_url = '/rsvp/'

    def form_valid(self, form):
        if (GuestCode.validate(form.cleaned_data["code"])):
            RSVPLogin.success_url = reverse('rsvp', kwargs={'code': str(form.cleaned_data["code"])})
        else:
            RSVPLogin.success_url = '/rsvp/'
        return super(RSVPLogin, self).form_valid(form)


class RSVP(TemplateView):
    template_name = "rsvp.html"
