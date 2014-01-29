from fanfics.models import FanFic
from django.forms import ModelForm

class CreateNewForm(ModelForm):
	class Meta:
		model = FanFic
		exclude = ['pub_date']