{"filter":false,"title":"urls.py","tooltip":"/murder_mystery/urls.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":15,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index)","]"],"id":3},{"start":{"row":15,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\")","]"]}],[{"start":{"row":15,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\")","]"],"id":4},{"start":{"row":15,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\")","]"]}],[{"start":{"row":15,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\")","]"],"id":5},{"start":{"row":15,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login, registration","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\"),","    url(r'^accounts/register/$', registration, name=\"registration\")","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":15},"end":{"row":19,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585838096614,"hash":"15c010ccffb442d7ebeb37007b9adc5a9a85a64b"}