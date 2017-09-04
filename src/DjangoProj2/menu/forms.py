from django import forms
from menu.models import Item
from bars_app.models import Bars_Location_Model

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields= [
			'bars',
			'name',
			'contents',
			'excludes',
			'public',
		]
	# def __init__(self, user=None, *args, **kwargs):
	def __init__(self,user=None, *args, **kwargs):
		#print(kwargs.pop('user'))
		#self.user = kwargs.pop('user')
		print(user)
		#self.user = kwargs.pop("user")
		#print(kwargs.pop('instance'))
		print(kwargs)
		super(ItemForm, self).__init__(*args, **kwargs)
		# self.fields['bars'].queryset = Bars_Location_Model.objects.none()
		self.fields['bars'].queryset = Bars_Location_Model.objects.filter(owner=user) #.exclude(item__isnull = False)

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == 'hello':
			raise forms.ValidationError("Not a valid name")
		return name	