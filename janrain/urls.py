from django.conf.urls.defaults import *

urlpatterns = patterns('janrain.views',
    url(r'^login/$', 'login', name='janrain-login'),
    url(r'^logout/$', 'logout', name='janrain-logout'),
    url(r'^loginpage/$', 'loginpage', name='janrain-loginpage'),
)
