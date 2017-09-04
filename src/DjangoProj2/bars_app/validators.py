from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

def clean_email(value):
	email = value
	if ".edu" in email:
		raise ValidationError("We do not accept the 'edu' emails ")

CUISINES = ['Mexican', 'Italian', 'American', 'Chinese', 'North Indian', 'South Indian','Asian Fusion']

def validate_cuisines(value):
	cuisine = value.capitalize()  #returns a copy of the string with first letter capitalized
	print(cuisine)
	if not cuisine in CUISINES and not value in CUISINES:
		raise ValidationError("{value} Not a valid Cuisine")
	#svalue = cuisine #for capitalizing the value before going to database

