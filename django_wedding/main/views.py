# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import RSVPLoginForm, GuestRSVPForm
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
            RSVPLogin.success_url = reverse('rsvp', kwargs={'code': form.cleaned_data["code"].lower()})
        else:
            RSVPLogin.success_url = '/rsvp/'
        return super(RSVPLogin, self).form_valid(form)


class RSVP(FormView):
    template_name = 'rsvp.html'

    def get(self, request, *args, **kwargs):
        print(kwargs["code"])

        code = GuestCode.objects.get(code=kwargs["code"])
        print("Code : %s (%s)" % (code, type(code)))
        print(code.guests.all())

        contact_form = ContactForm()
        contact_form.prefix = 'contact_form'
        social_form = SocialForm()
        social_form.prefix = 'social_form'
        return self.render_to_response(self.get_context_data({'contact_form':contact_form, 'social_form':social_form}))

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(self.request.POST, prefix='contact_form')
        social_form = SocialForm(self.request.POST, prefix='social_form ')

        if contact_form.is_valid() and social_form.is_valid():
            ### do something
            return HttpResponseRedirect("/thanks/")
        else:
            return self.form_invalid(contact_form,social_form , **kwargs)


    def form_invalid(self, contact_form, social_form, **kwargs):
        contact_form.prefix='contact_form'
        social_form.prefix='social_form'
        return self.render_to_response(self.get_context_data({'contact_form':contact_form,
                                                             'social_form':social_form }))
