from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.home_list, name='home_list'),
    url(r'^homesection/new/$', views.homeSection_new, name='homeSection_new'),
    url(r'^algsection/new/$', views.algSection_new, name='algSection_new'),
    url(r'^section/(?P<pk>\d+)/$', views.homeSection_detail, name='homeSection_detail'),

    #url(r'^$', views.HomePageView.as_view(), name='home'), ### using static home

    url(r'^algs/$', views.AlgsPageView.as_view(), name='algs'), 
    url(r'^biblio/$', views.BiblioPageView.as_view(), name='biblio'),
    url(r'^biblio/algorithms/$', views.BiblioPageView.as_view(), name='b-algs'),
]
