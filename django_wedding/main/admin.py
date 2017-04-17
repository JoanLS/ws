# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import Guest, GuestCode, GuestChildren
# Register your models here.

admin.site.register(Guest)
admin.site.register(GuestCode)
admin.site.register(GuestChildren)
