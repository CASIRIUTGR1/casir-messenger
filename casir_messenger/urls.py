from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'casir_messenger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', "user_manager.views.index", name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^friends/', include('friends.urls')),
)
