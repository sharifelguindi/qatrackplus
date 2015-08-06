from django.conf.urls import patterns, url
from qatrack.pim import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^form', views.pimform, name='pimform'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^review/table/(?P<dept>\w+)/$', views.pimreview_table_dept, name='pim_dept_review'),
    url(r'^review/table/$', views.pimreview_table, name='pimreview_table'),
    url(r'^review/bar', views.pimreview_bar, name='pimreview_bar'),
    
    
)
