# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import RSVPLoginForm, GuestRSVPForm, GuestCommentsForm, GuestChildrenForm
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


class RSVP(TemplateView):
    template_name = 'rsvp.html'

    def get(self, request, *args, **kwargs):
        print(kwargs["code"])

        code = GuestCode.objects.get(code=kwargs["code"])
        print("Code : %s (%s)" % (code, type(code)))
        print(code.guests.all())

        guest_forms = []
        guests = []
        for guest in code.guests.all():
            guests.append(guest)
            guest_forms.append(GuestRSVPForm(instance=guest))

        context = self.get_context_data(**kwargs)
        context['guests'] = guests
        context['guest_forms'] = guest_forms
        context['comments_form'] = GuestCommentsForm(instance=code.comments.first())
        context['children_form'] = GuestChildrenForm(instance=code.children.first())


        return self.render_to_response(context)
