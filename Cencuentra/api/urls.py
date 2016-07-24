from django.conf.urls import url
from . import views as api_view

urlpatterns = [
    #User urls
    url(r'user/register$', api_view.UserRegisterView.as_view(), name='user_api'),
    url(r'user/$', api_view.UserView.as_view(), name='myuser_api'),
    url(r'user/(?P<pk>[0-9]+)/$', api_view.UserDetailView.as_view(), name='myuser_api_detail'),
    
    url(r'negocio/$', api_view.NegocioView.as_view(), name='negocio_api'),
    url(r'negocio/(?P<pk>[0-9]+)/$', api_view.NegocioDetailView.as_view(), name='negocio_api_detail'),
    
    ]