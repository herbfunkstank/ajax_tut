This is an update the Django, jQuery, & Ajax tutorial series from: http://lethain.com/intro-to-unintrusive-javascript-with-django/
I didn't write the original tutorial.  The original git can be found: https://github.com/lethain/notes-djapp-tutorial 

The original is 4 year old.  I build the tutorial app with Django 1.4.2
With the changes you will find here, you can get the tutorial 
working with Django 1.4.2.

﻿Fixed an error with 'ajax_tut/ajax_tut/urls.py':
Deleted ajax_tut from:  (r'^', include('ajax_tut.notes.urls')), 
Made it work as:        (r'^', include('notes.urls')),

Fixed the error causing CSRF Cross Site Forgery errors (403) Forbidden whenever using the create function:
Added csrf_token template tag so the create function actually works instead of returning CSRF Cross Site Forgery errors (403 Forbidden).  
Needed to add {% csrf_token %} within the form tags.  
Added to templates: 'ajax_tut/notes/templates/notes/note_detail.html' and 'ajax_tut/notes/templates/notes/note_list.html'.

I noticed an error with the note details page when trying to update a note that it can't find.
