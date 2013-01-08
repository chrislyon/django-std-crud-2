from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj1.views.home', name='home'),
    # url(r'^dj1/', include('dj1.foo.urls')),

	## Home
    url(r'^$', 'dj1.views.index', name='home'),
    url(r'^about/$', 'dj1.views.about', name='about'),
    url(r'^contact_us/$', 'dj1.views.contact_us', name='contact_us'),

	# Authentification : login
	url(r'^cnx/', include('cnx.urls')),
	#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'tmpl/login.html', }, name='login'),
	#url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'tmpl/logout.html', }, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	## Gestion des fichiers Xchange
    url(r'^fx/', include('fx.urls')),

	## Pour Test
    url(r'^tst/', include('tst.urls')),

	## Pour Test
    url(r'^contact/', include('contact.urls')),

)
