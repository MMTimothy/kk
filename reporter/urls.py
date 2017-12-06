from . import views
from django.conf.urls import url,include

urlpatterns =[
    url('', include('pwa.urls')),
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^checkin/$',views.checkin.as_view(),name='checkin'),
    url(r'^checkout/$',views.checkout.as_view(),name='checkout'),
    url(r'^supervisor/$',views.supervisor.as_view(), name='supervisor'),
    url(r'^guardmap',views.guardmap.as_view(),name='guardmap')

]