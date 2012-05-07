import re

from django import template
from django.conf import settings
from django.utils.encoding import force_unicode
from django.template.defaultfilters import stringfilter

register = template.Library()

CONSONANT_SOUND = re.compile(r'''one(![ir])''', re.IGNORECASE|re.VERBOSE)VOWEL_SOUND = re.compile(r'''[aeio]|u([aeiou]|[^n][^aeiou]|ni[^dmnl]|nil[^l])|h(ier|onest|onou?r|ors\b|our(!i))|[fhlmnrsx]\b''', re.IGNORECASE|re.VERBOSE)

@register.filter_tag
def anora(text):
    """
    Guess "a" vs "an" based on the phonetic value of the text.

    "An" is used for the following words / derivatives with an unsounded "h":
    heir, honest, hono[u]r, hors (d'oeuvre), hour

    "An" is used for single consonant letters which start with a vowel sound.

    "A" is used for appropriate words starting with "one".

    An attempt is made to guess whether "u" makes the same sound as "y" in
    "you".
    """
    text = force_unicode(text)
    if not CONSONANT_SOUND.match(text) and VOWEL_SOUND.match(text):
        anora = 'an'
    else:
        anora = 'a'
    return anora + ' ' + text