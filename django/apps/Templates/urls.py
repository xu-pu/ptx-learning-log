from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'LearningDjango.Templates.views',
    url(r'^(?P<title>.*)$', 'get_content'),
)
