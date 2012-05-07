Anora - Django templatetag
============================
Anora is a simple_tag that determines whether or not a word should have an "a" or "an" in front of it. Adds either one of these depending on the phoentic value of the given text. It will also automatically add one space before the text and 


Install
----------------------------
1. Add ``anora`` to your ``INSTALLED_APPS`` 
2. Add ``{% load anora %}`` to the top of templates you wish to use these tags in.


Usage
----------------------------
{% load anora %}

I was taking a walk in the woods today. I came across {{ animal_type|anora  }}.


Credits
----------------------------
Original template filter can he found [here](http://djangosnippets.org/snippets/1519/).