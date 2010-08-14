
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    """
    Polls the Twitter API for ratings with the #ratemyflight hashtag.
    """
    def handle_noargs(self, **options):
        pass

