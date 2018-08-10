from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.IndextView.as_view(), name='index' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),
    url(r'contractor/add/$', views.CreateCont.as_view(), name='contractor-add' ),
    url(r'cl/add/$', views.CreateCl.as_view(), name='cl-add' ),

]