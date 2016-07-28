# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# load admin modules
from django.contrib import admin
admin.autodiscover()


urls = [
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^webapp/', include('webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', admin.site.urls),
]
urlpatterns = urls

# static and media urls not works with DEBUG = True, see static function.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns.append(url(r'^_x\_debug__/', debug_toolbar.urls))

