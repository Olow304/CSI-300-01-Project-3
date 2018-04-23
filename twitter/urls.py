from django.conf.urls import patterns, include, url
#you can uncomment tne next two line to enable the admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
  url(r'^$', 'twitter_app.views.index'),
  url(r'^users/$', 'twitter_app.views.users'),
  url(r'^tweets$', 'twitter_app.views.public'),
  url(r'^submit$', 'twitter_app.views.submit'),
  url(r'^login$', 'twitter_app.views.login_view'),
  url(r'^logout$', 'twitter_app.views.logout_view'),
  url(r'^signup$', 'twitter_app.views.signup'),
  url(r'^users/(?P<username>\w{0,30})/$', 'twitter_app.views.users'),
  url(r'^follow$', 'twitter_app.views.follow'),
  url(r'^admin/', admin.site.urls),
  )
