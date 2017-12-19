from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.home_list, name='home_list'),
    url(r'^section/(?P<pk>\d+)/$', views.home_detail, name='home_detail'),
    url(r'^homesection/new/$', views.homeSection_new, name='homeSection_new'),
    url(r'^algsection/new/$', views.algSection_new, name='algSection_new'),
    url(r'^section/(?P<pk>\d+)/remove/$', views.section_remove, name='section_remove'),
    url(r'^section/(?P<pk>\d+)/edit/$', views.section_edit, name='section_edit'),

    #url(r'^$', views.HomePageView.as_view(), name='home'), ### using static home

    url(r'^algs/$', views.AlgsPageView.as_view(), name='algs'), 
    url(r'^biblio/$', views.BiblioPageView.as_view(), name='biblio'),
    url(r'^biblio/algorithms/$', views.BiblioPageView.as_view(), name='b-algs'),

    url(r'^backend/$', views.BackendPageView.as_view(), name='backend'), 

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^accounts/', include('django.contrib.auth.urls')),

    #url(r'^login/$', auth_views.login, {'backend': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'backend': 'logout.html'}, name='logout'),

]
