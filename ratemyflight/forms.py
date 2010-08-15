
from django import forms

from ratemyflight.models import Rating


class RatingForm(forms.ModelForm):

    email = forms.EmailField(_("Email"), required=False, 
        help_text="Only used to retrieve your gravatar icon.")
    value = forms.FloatField(max_value=10, min_value=0)

    class Meta:
        model = Rating
        exclude = ("avatar_url", "time", "tweet_id", "tweet_text")

