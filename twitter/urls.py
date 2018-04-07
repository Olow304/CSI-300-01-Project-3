from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url, include
import twitter.views
from django.contrib import admin

urlpatterns = [
    url(r'^$', twitter.views.home_page, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
