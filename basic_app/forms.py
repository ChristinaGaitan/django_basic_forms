from django import forms

class FormName(froms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  text = forms.CharField(widget = forms.Textarea)
