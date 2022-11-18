from django import forms
from django.forms import widgets
from webapp.models import Type, Status


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Summary')
    description = forms.CharField(max_length=2000, required=False, label='Description',
                                  widget=widgets.Textarea(attrs={
                                      "cols": 22,
                                      "rows": 3
                                  }))
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')
    status = forms.ModelChoiceField(queryset=Status.objects.all())