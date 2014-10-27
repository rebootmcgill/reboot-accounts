from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #url(r'^$', UnfilledRequestsList.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
)
