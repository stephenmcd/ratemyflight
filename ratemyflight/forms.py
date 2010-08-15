
from django import forms

from ratemyflight.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        

