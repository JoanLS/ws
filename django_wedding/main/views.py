# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import RSVPLoginForm, GuestRSVPForm, GuestCommentsForm, GuestChildrenForm
from django.urls import reverse
from main.models import GuestCode
from django.utils.translation import ugettext as _


class Homepage(TemplateView):
    template_name = "home.html"


class FAQ(TemplateView):
    template_name = "faq.html"


class Practical(TemplateView):
    template_name = "practical.html"


class ThankYou(TemplateView):
    template_name = "thanks.html"


class RSVPLogin(FormView):
    template_name = 'rsvp_login.html'
    form_class = RSVPLoginForm
    success_url = "/faq/"

    def form_valid(self, form):
        print("Form is valid!")
        if (GuestCode.validate(form.cleaned_data["code"])):
            RSVPLogin.success_url = reverse(
                'rsvp', kwargs={'code': form.cleaned_data["code"].lower()})
        else:
            form.add_error(None, _("Sorry, the code you entered is invalid."))
            return super(RSVPLogin, self).form_invalid(form)
        return super(RSVPLogin, self).form_valid(form)


class RSVP(TemplateView):
    template_name = 'rsvp.html'

    def get(self, request, *args, **kwargs):
        print(kwargs["code"])

        code = GuestCode.objects.get(code__iexact=kwargs["code"])
        print("Code : %s (%s)" % (code, type(code)))
        print(code.guests.all())

        guest_forms = []
        guests = []
        for guest in code.guests.all():
            guests.append(guest)
            guest_forms.append(
                GuestRSVPForm(instance=guest, prefix="guest" + str(guest.id)))

        context = self.get_context_data(**kwargs)
        context['guests'] = guests
        context['guest_forms'] = guest_forms
        context['comments_form'] = GuestCommentsForm(
            instance=code.comments.first(), prefix="comments")
        context['children_form'] = GuestChildrenForm(
            instance=code.children.first(), prefix="children")

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        code = GuestCode.objects.get(code__iexact=kwargs["code"])

        guest_forms = []
        guests = []
        for guest in code.guests.all():
            guest_form = GuestRSVPForm(
                request.POST, instance=guest, prefix="guest" + str(guest.id))
            if guest_form.is_valid():
                guest_form.save()

        comments_form = GuestCommentsForm(
            request.POST, instance=code.comments.first(), prefix="comments")
        children_form = GuestChildrenForm(
            request.POST, instance=code.children.first(), prefix="children")
        if children_form.is_valid():
            guest_children = children_form.save(commit=False)
            guest_children.code = code
            guest_children.save()

        if comments_form.is_valid():
            guest_comments = comments_form.save(commit=False)
            guest_comments.code = code
            guest_comments.save()

        code.responded = True
        code.save()
        return redirect(reverse('thankyou'))
