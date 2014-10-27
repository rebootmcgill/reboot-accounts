from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    #url(r'^$', UnfilledRequestsList.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^register/$', CreateView.as_view(
            template_name='accounts/registration.html',
            form_class=UserCreationForm,
            success_url='/'
    ), name="Registration"),

)
