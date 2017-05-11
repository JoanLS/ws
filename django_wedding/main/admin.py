# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import Guest, GuestCode, GuestChildren, GuestComments

# Register your models here.


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'code',
                    'coming_private_ceremony', 'coming_public_ceremony',
                    'coming_reception', 'coming_dinner', 'coming_party')
    list_filter = ('coming_private_ceremony', 'coming_public_ceremony',
                   'coming_reception', 'coming_dinner', 'coming_party')


class GuestAdminInline(admin.TabularInline):
    model = Guest
    extra = 0


class GuestChildrenAdminInline(admin.TabularInline):
    model = GuestChildren
    max_num = 1


class GuestCommentsInlineAdmin(admin.StackedInline):
    model = GuestComments
    max_num = 1


class GuestCodeAdmin(admin.ModelAdmin):
    inlines = (GuestAdminInline, GuestChildrenAdminInline,
               GuestCommentsInlineAdmin)


class GuestCommentsAdmin(admin.ModelAdmin):
    list_display = ('code', 'dietary_restrictions', 'music_request',
                    'comments')


admin.site.register(Guest, GuestAdmin)
admin.site.register(GuestCode, GuestCodeAdmin)
admin.site.register(GuestChildren)
admin.site.register(GuestComments, GuestCommentsAdmin)
