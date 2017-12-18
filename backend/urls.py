from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.home_list, name='home_list'),
    url(r'^$', views.HomePageView.as_view(), name='home'), 
    url(r'^algs/$', views.AlgsPageView.as_view(), name='algs'), 
    url(r'^biblio/$', views.BiblioPageView.as_view(), name='biblio'),
    url(r'^biblio/algorithms/$', views.BiblioPageView.as_view(), name='b-algs'),
    #url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]
