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
]