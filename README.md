Anora
==========================
Anora is a Django template filter that determines whether or not a word should have an "a" or "an" in front of it. Adds either one of these depending on the phoenetic value of the given text. It will also automatically add one space before the text.

Install
-------

1. ``pip install anora``
2. Add ``anora`` to your ``INSTALLED_APPS`` 
3. Add ``{% load anora %}`` to the top of templates you wish to use these tags in.

Usage
-------
``{% load anora %}``

``I was taking a walk in the woods today. I came across {{ animal_type|anora  }}.``

Possible outcomes from the above:
-------

I was taking a walk in the woods today. I came across a raccoon.

I was taking a walk in the woods today. I came across an owl.

Credits
-------
Original template filter can he found [here](http://djangosnippets.org/snippets/1519/).