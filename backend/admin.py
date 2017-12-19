# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin

# Register your models here.

from .models import Section
#, SectionR, other models

admin.site.register(Section)
#admin.site.register(SectionR)
#admin.site.register(AlgsL)
#admin.site.register(etc)