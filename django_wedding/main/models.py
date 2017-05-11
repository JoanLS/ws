# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class GuestCode(models.Model):
    code = models.CharField(max_length=6)
    responded = models.BooleanField(default=False)

    def __unicode__(self):
        return self.code

    @staticmethod
    def validate(code):
        code = code.lower()
        return GuestCode.objects.filter(code=code).count() > 0


class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    code = models.ForeignKey(GuestCode, related_name='guests')
    invited_private_ceremony = models.BooleanField(default=False)
    invited_public_ceremony = models.BooleanField(default=False)
    invited_reception = models.BooleanField(default=False)
    invited_dinner = models.BooleanField(default=False)
    invited_party = models.BooleanField(default=False)
    coming_private_ceremony = models.BooleanField(default=False)
    coming_public_ceremony = models.BooleanField(default=False)
    coming_reception = models.BooleanField(default=False)
    coming_dinner = models.BooleanField(default=False)
    coming_party = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class GuestChildren(models.Model):
    children_menus = models.IntegerField(default=0)
    code = models.ForeignKey(GuestCode, related_name='children')


class GuestComments(models.Model):
    dietary_restrictions = models.CharField(max_length=500, blank=True)
    music_request = models.CharField(max_length=500, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    code = models.ForeignKey(GuestCode, related_name='comments')
