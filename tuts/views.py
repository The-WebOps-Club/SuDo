#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from tuts.models import Tutsheet
from django.views.generic.list import ListView

class FileListView(ListView):
    model = Tutsheet
    # queryset = Tutsheet.objects.order_by('-id')
    # context_object_name = "files"
    # template_name = "tuts/tutsheet_list.html"