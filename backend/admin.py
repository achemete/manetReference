# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin

# Register your models here.

from .models import Section

admin.site.register(Section)