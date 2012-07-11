import re

from django import template
from django.conf import settings
from django.utils.encoding import force_unicode
from django.template.defaultfilters import stringfilter

register = template.Library()

CONSONANT_SOUND = re.compile(r'''one(![ir])''', re.IGNORECASE|re.VERBOSE)
VOWEL_SOUND = re.compile(r'''[aeio]|u([aeiou]|[^n][^aeiou]|ni[^dmnl]|nil[^l])|h(ier|onest|onou?r|ors\b|our(!i))|[fhlmnrsx]\b''', re.IGNORECASE|re.VERBOSE)

@register.filter
def anora(text):
    text = force_unicode(text)
    anora = 'an' if not CONSONANT_SOUND.match(text) and VOWEL_SOUND.match(text) else 'a'
    return anora + ' ' + text