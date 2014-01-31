from fanfics.models import FanFic
from django.forms import ModelForm
from django import forms

class CreateNewForm(ModelForm):
	class Meta:
		model = FanFic
		exclude = ['pub_date','url','profile']
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style':'width:600px; margin:0 auto; '}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'style':'width:600px; margin:0 auto; '}),
            'fandom': forms.TextInput(attrs={'class': 'form-control', 'style':'width:600px; margin:0 auto; '}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'style':'width:600px; margin:0 auto; '}),

        }

class CreateURLForm(ModelForm):
	class Meta:
		model = FanFic
		fields = ['url']
		widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'style':'width:800px; margin:0 auto; '}),
        }
	def __init__(self, *args, **kwargs):
		super(CreateURLForm, self).__init__(*args, **kwargs)
		self.fields['url'].label = ""