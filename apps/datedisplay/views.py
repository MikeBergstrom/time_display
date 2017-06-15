# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render

def index(request):
    print "in index"
    context = {
        'time' : datetime.datetime.now()
    }
    print context
    return render(request, 'datedisplay/index.html', context)
# Create your views here.
