from django import forms

class MatricForm(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField()

class ImperialForm(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField()