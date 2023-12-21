from django import forms
from django.core.validators import ValidationError

from blog_app.models import Message


class ContactUs(forms.Form):
    YOUR_TYPE_CHOICES = ['Blogger', 'Viewer']

    choices_field = forms.ChoiceField(widget=forms.RadioSelect, choices=YOUR_TYPE_CHOICES)
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(max_length=300)

    def clean(self):
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')

        if subject == message:
            raise ValidationError('subject and message are same')

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if '@' in name:
            raise ValidationError('You can not use @ in your name')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'title', 'text')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your title',
                'style': 'max-width: 500px'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Email',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your title',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text',
            })

        }
