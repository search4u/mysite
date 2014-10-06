from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mysite.views',
	url(r'^$','hello'),
	url(r'^time/$','current_datetime'),
	url(r'^time/plus/(?P<offset>\d{1,2})$','hours_ahead'),
)
urlpatterns += patterns('mysite.books.views',
	url(r'^search/$','search'),
)
urlpatterns += patterns('mysite.contact.views',
    url(r'^contact/$','contact'),
    url(r'^contact/thanks/$','thanks'),
)
