from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^$', views.index, name='index'),

    # ---  Home Views  --- #
    
    # -- listing
    url(r'^$', views.home_list, name='home_list'),
    url(r'^section/(?P<pk>\d+)/$', views.home_detail, name='home_detail'),
    url(r'^sectionr/(?P<pk>\d+)/$', views.homeR_detail, name='homeR_detail'),

    # -- creation
    url(r'^homesection/new/$', views.homeSection_new, name='homeSection_new'),
    url(r'^homesectionr/new/$', views.homeSectionRight_new, name='homeSectionRight_new'), #new added
    
    # -- mod/rem
    url(r'^section/(?P<pk>\d+)/remove/$', views.section_remove, name='section_remove'),
    url(r'^section/(?P<pk>\d+)/edit/$', views.section_edit, name='section_edit'),
    url(r'^sectionr/(?P<pk>\d+)/remove/$', views.sectionR_remove, name='sectionRight_remove'),
    url(r'^sectionr/(?P<pk>\d+)/edit/$', views.sectionR_edit, name='sectionRight_edit'),

    # --- Algorithms Views --- #
    
    # -- listing
    #url(r'^$', views.alg_list, name='alg_list'),
    #url(r'^algs/$', views.AlgsPageView.as_view(), name='algs'), 
    url(r'^algorithms/$', views.algos_list, name='algos_list'),
    url(r'^algol/(?P<pk>\d+)/$', views.algol_detail, name='algol_detail'),
    url(r'^algor/(?P<pk>\d+)/$', views.algor_detail, name='algor_detail'),

    # -- creation
    url(r'^algright/new/$', views.algRight_new, name='algRight_new'),
    url(r'^algleft/new/$', views.algLeft_new, name='algLeft_new'), 
    
    # -- mod/rem
    url(r'^algleft/(?P<pk>\d+)/remove/$', views.algLeft_remove, name='algLeft_remove'),
    url(r'^algleft/(?P<pk>\d+)/edit/$', views.algLeft_edit, name='algLeft_edit'),
    url(r'^algright/(?P<pk>\d+)/remove/$', views.algRight_remove, name='algRight_remove'),
    url(r'^algright/(?P<pk>\d+)/edit/$', views.algRight_edit, name='algRight_edit'),


    # --- Bibliography Views --- #

    url(r'^biblio/$', views.BiblioPageView.as_view(), name='biblio'),
    url(r'^biblio/algorithms/$', views.BiblioPageView.as_view(), name='b-algs'),


    # --- Backend Views --- #

    # -- regular operations

    url(r'^backend/$', login_required(views.BackendPageView.as_view()), name='backend'), 
    url(r'^backend/operations$', views.OperationsPageView.as_view(), name='operations'), 
    url(r'^backend/users$', views.list_users, name='list_users'), 

    # -- content administration

    #url(r'^$', views.home_list, name='home_list'), -----> list all homes content in a table
    #url(r'^algorithms/$', views.algos_list, name='algos_list'), -----> list all algorithms' content in a table



    # --- Other Views --- #

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    #url(r'^login/$', auth_views.login, {'backend': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'backend': 'logout.html'}, name='logout'),

]
