#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Tutsheet(models.Model):
	"""
	Model for uploading Tutsheet.
	"""
	filename = models.FileField(upload_to='media/tuts')
	verbose_name = models.CharField(max_length = 50)

class Gist(models.Model):
	"""
	Model for uploading Gists/Assignments 
	"""
	name = models.CharField(max_length = 50)
	desc = models.TextField()

class GistSubmission(models.Model):
	"""
	Model for uploading submissions for gists
	"""
	gist = models.ForeignKey(Gist)
	user = models.ForeignKey(User)
	filename = models.FileField(upload_to='media/gists')

class Attend(models.Model):
	"""
	Model for attendance
	"""
	user = models.ForeignKey(User)
	date = models.DateField(auto_now_add=True)
	ip = models.CharField(max_length=20)

class Proxy(models.Model):
	"""
	Model for proxy
	"""
	user_by = models.CharField(max_length=50)
	user_for = models.CharField(max_length=50)
	date = models.DateField(auto_now_add=True)
	ip = models.CharField(max_length=20)