"""itu_rover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from about.views import AboutPage
from members.views import MembersPage
from main.views import MainPage
from rover.views import RoverPage
from sponsors.views import SponsorsPage
from old_rover.views import OldRoverPage

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('hakkında/', AboutPage.as_view(), name='about'),
    path('takım-üyeleri/', MembersPage.as_view(), name='members'),
    path('sponsorlar/', SponsorsPage.as_view(), name='sponsors'),
    path('rover/', RoverPage.as_view(), name='rover'),
    path('destek-ol/', MembersPage.as_view(), name='support'),
    path('medya/', MembersPage.as_view(), name='media'),
    path('Eski roverlar',OldRoverPage.as_view(), name='oldrover'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = ([
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
