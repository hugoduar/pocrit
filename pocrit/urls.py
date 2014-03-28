from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pocrit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','critica.views.category_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/', 'critica.views.category'),
)
