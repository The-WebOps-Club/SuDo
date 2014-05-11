from django import forms
from tuts.models import GistSubmission

class GistSubmissionForm(forms.ModelForm):
	class Meta:
		model = GistSubmission
		widgets = {'gist':forms.HiddenInput(),'user':forms.HiddenInput()}