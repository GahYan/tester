from django.conf.urls import url, include
from django.contrib import admin
from search import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [



    url(r'^$', views.search,name='search'),
    url(r'^(?P<url_title>.*)/$', views.detail, name='detail'),




]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
