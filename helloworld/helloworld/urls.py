from django.conf.urls import *
from helloworld.view import hello
from helloworld.testdb import testdb
from helloworld.search import *
from helloworld import search2

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
		('^hello/$',hello),
		('^testdb/$', testdb),
		(r'^search_form/$', search_form),
		(r'^search/$', search),
		(r'^search-post/$', search2.search_post),
		url(r'^admin/', include(admin.site.urls)),
		url(r'^Users/', include('Users.urls')),
	)