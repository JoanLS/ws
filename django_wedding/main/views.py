# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "home.html"


class RSVPLogin(TemplateView):
    template_name = "rsvp_login.html"
