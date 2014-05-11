#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from tuts.models import Gist, GistSubmission
from django.forms.models import modelformset_factory
from django.conf import settings
from tuts.forms import *
import datetime
from tuts.models import Attend, Proxy

def home(request):
	"""
	This view is for the basic landing page of the website.
	"""
	if request.user.is_authenticated():
		return redirect(settings.SITE_URL + 'gistsubmit/')
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))

# def gistsubmit(request):
# 	"""
# 	This view is for receiving the GistSubmissions
# 	"""
# 	gists = Gist.objects.all()
# 	GistSubmissionFormSet = modelformset_factory(GistSubmission, fields=('filename','verbose_name'), extra=0)
# 	if request.method == "POST":
# 		formset = GistSubmissionFormSet(request.POST,request.FILES, queryset = gists)
# 		if formset.is_valid():
# 			assert False
# 	else:
# 		formset = GistSubmissionFormSet(queryset=Gist.objects.all())
# 	gistData = zip(gists, formset)
# 	return render_to_response('gistsubmit.html', locals(), context_instance = RequestContext(request))	

def gistsubmit(request):
	"""
	This view is for receiving the GistSubmissions
	"""
	gists = Gist.objects.all()
	if request.method == "POST":
		formset = []
		gist = int(request.POST.get("gist",0))
		try:
			form = GistSubmissionForm(request.POST, request.FILES, instance = GistSubmission.objects.get(id=gist))
		except GistSubmission.DoesNotExist:
			form = GistSubmissionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(settings.SITE_URL + "gistsubmit/")
		else:
			for g in gists:
				if g.id == gist:
					formset.append(form)
				else:
					formset.append(GistSubmissionForm(initial = {'gist':g,'user':request.user,}))
	else:
		formset = []
		for g in gists:
			try:
				form = GistSubmissionForm(instance = GistSubmission.objects.get(gist=g,user=request.user))
			except GistSubmission.DoesNotExist:
				form = GistSubmissionForm(initial = {'gist':g,'user':request.user,})
			formset.append(form)
	gistData = zip(gists, formset)
	return render_to_response('gistsubmit.html', locals(), context_instance = RequestContext(request))

def attend(request):
	alllogs = Attend.objects.filter(date = datetime.date.today(), ip = request.META['REMOTE_ADDR'])
	if len(alllogs) > 0:
		if alllogs[0].user ==  request.user:
			return HttpResponse("<p>Your attendance was already recorded!</p>")	
		else:
			pr = Proxy(user_by = alllogs[0].user.username, user_for = request.user.username, date = datetime.date.today(), ip = request.META['REMOTE_ADDR'])
			pr.save()
			return HttpResponse("<p>Don't put proxy!-_- The Club Convenors have been notified!</p>")
	else:
		attendance = Attend(user=request.user, ip = request.META['REMOTE_ADDR'])
		attendance.save()
		return HttpResponse("<p>Your attendance has been recorded successfully!</p>")
	