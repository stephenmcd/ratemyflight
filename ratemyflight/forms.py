
from hashlib import md5

from django import forms
from django.utils.translation import ugettext_lazy as _

from ratemyflight.models import Rating
from ratemyflight.settings import GRAVATAR_SIZE


class RatingForm(forms.ModelForm):

    email = forms.EmailField(label=_("Email"), required=False, 
        help_text="Only used to retrieve your gravatar icon.")
    value = forms.FloatField(label=_("Rating"), help_text="From 1 to 10", 
        max_value=10, min_value=0)

    class Meta:
        model = Rating
        exclude = ("avatar_url", "time", "tweet_id", "tweet_text")

    def __init__(self, *args, **kwargs):
        """
        Set fields as required.
        """
        super(RatingForm, self).__init__(*args, **kwargs)
        for (name, field) in self.fields.items():
            if name != "email":
                field.required = True

    def save(self):
        """
        Set the avatar's URL using gravatar and the given email address.
        """
        rating = super(RatingForm, self).save()
        email = self.cleaned_data.get("email")
        if email:
            rating.avatar_url = "http://www.gravatar.com/avatar/%s?s=%s" % \
                (md5(email).hexdigest(), GRAVATAR_SIZE)
            rating.save()

