from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm', views.confirm, name='confirm'),
    path('pay', views.pay, name='pay'),
    path('success', views.success, name='success'),
    path('callback', csrf_exempt(views.callback), name="callback"),
    path('charge-status/', views.charge_status),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('withdrawal-status/', views.withdrawal_status),
]
