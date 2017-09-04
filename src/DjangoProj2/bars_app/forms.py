from django import forms

from .models import Bars_Location_Model
from .validators import validate_cuisines
 
class BarsCreateForm(forms.Form):
	 	name 	  = forms.CharField()
		location  = forms.CharField(required=False)
		cuisines  = forms.CharField(required=False)

		def clean_name(self):
			name = self.cleaned_data.get('name')
			if name == "hello":
				raise forms.ValidationError("Not a valid name")
			return name 

class BarsLocationModelCreateForm(forms.ModelForm):
	#email = forms.EmailField()
	#cuisines = forms.CharField(required=False,validators=[validate_cuisines])
	class Meta:
		model = Bars_Location_Model
		fields = [
			'name',
			'location',
			'cuisines',
			#'slug',
		]

	def __init__(self,owner=None, *args, **kwargs):
		#print(kwargs.pop('user'))
		print(owner)
		super(BarsLocationModelCreateForm, self).__init__(*args, **kwargs)
		#self.fields['bars'].queryset = Bars_Location_Model.objects.filter(owner=user)

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == "hello":
			#print('hello')
			raise forms.ValidationError("Not a valid name")
		return name 

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	if ".edu" in email:
	# 		raise forms.ValidationError("We do not accept the 'edu' emails ")
	# 	return email

