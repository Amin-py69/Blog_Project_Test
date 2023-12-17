from django import forms


class ContactUs(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(max_length=300)
