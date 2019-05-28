from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    sal  = forms.IntegerField()
    email = forms.CharField(max_length=50)

one
qqqq