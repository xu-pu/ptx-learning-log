from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'LearningDjango.authenticate.views',

    url(r'^$', 'state_view'),
    url(r'^login$', 'login_view'),
    url(r'^register$', 'register_view'),
    url(r'^logout$', 'logout_view'),
    url(r'^state$', 'state_view'),
    url(r'^content$', 'content_view'),

)
