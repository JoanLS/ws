"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import Homepage, RSVPLogin, RSVP, FAQ, Practical

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Homepage.as_view(), name="home"),
    url(r'^faq/$', FAQ.as_view(), name="faq"),
    url(r'^info/$', Practical.as_view(), name="practical"),
    url(r'^rsvp/$', RSVPLogin.as_view(), name="rsvp_login"),
    url(r'^rsvp/(?P<code>[a-zA-Z]{3}[0-9]{3})/$', RSVP.as_view(), name="rsvp")
]
