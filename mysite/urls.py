
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from search import views


urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home,name='home'),

    url(r'^search/', include('search.urls'), name='include_search'),

    url(r'^blog/$', views.blog, name='blog'), ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
