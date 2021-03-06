from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),  
    url(r'^post/pdf/$', views.some_view, name='some_view'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^drag/$', views.drag, name='drag'),  
    url(r'^post/doc_base/$', views.doc_base, name='doc_base'),
    url(r'^post/tabella/$', views.tabella, name='tabella'),
    
    url(r'^soggetto/new/$', views.soggetto_new, name='soggetto_new'),
    url(r'^soggetto/(?P<pk>[0-9]+)/$', views.soggetto_detail, name='soggetto_detail'), 
    url(r'^soggetto/(?P<pk>[0-9]+)/edit/$', views.soggetto_edit, name='soggetto_edit'),
    
    url(r'^gara/new/$', views.gara_new, name='gara_new'),
    url(r'^gara/(?P<pk>[0-9]+)/$', views.gara_detail, name='gara_detail'),  
    url(r'^gara/(?P<pk>[0-9]+)/edit/$', views.gara_edit, name='gara_edit'),
    
    url(r'^azienda/new/$', views.azienda_new, name='azienda_new'),
    url(r'^azienda/(?P<pk>[0-9]+)/$', views.azienda_detail, name='azienda_detail'), 
    url(r'^azienda/(?P<pk>[0-9]+)/edit/$', views.azienda_edit, name='azienda_edit'), 
]