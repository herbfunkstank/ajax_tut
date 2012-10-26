from django.conf.urls.defaults import *
from django.conf import settings
urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^', include('notes.urls')),
)
