from django.conf.urls import patterns, include, url

urlpatterns = patterns('LearningDjango.blog.views',
    url(r'^index$', include('LearningDjango.Templates.urls')),
)
