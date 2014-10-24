from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^add_building$', 'tag.views.add_building', name='add_building'),
    url(r'^add_other', 'tag.views.add_other', name='add_other'),
    url(r'^add_path', 'tag.views.add_path', name='add_path'),
    url(r'^get_path', 'tag.views.get_path', name='get_path'),
    url(r'^get_other', 'tag.views.get_other', name='get_other'),
    url(r'^get_building', 'tag.views.get_building', name='get_building'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
